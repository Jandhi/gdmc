import itertools
from ..districts.district import District
from gdpc import Editor, WorldSlice, Block
from gdpc.vector_tools import ivec2, ivec3, Rect
from ..terrain.set_height import set_height
from ..terrain.smooth import average_neighbour_height, update_district_points
from ..core.utils.bounds import is_in_bounds2d

DISTRICT_AVG_RATIO = (
    0.5  # the percent of the height that the districts average should influence
)
EDGE_RANGE = 5  # how far in both directions the edges are smoothed


def smooth_edges(
    build_rect: Rect,
    districts: list[District],
    district_map: list[list[District]],
    world_slice: WorldSlice,
    editor: Editor,
    water_map: list[list[bool]],
):
    print("Smoothing edges")

    points = set()

    for district in districts:
        if not district.is_urban:  # only need to smooth edges for urban areas
            continue

        for edge in district.edges:
            for dx, dz in itertools.product(
                range(-EDGE_RANGE, EDGE_RANGE), range(-EDGE_RANGE, EDGE_RANGE)
            ):
                pt = ivec2(edge.x + dx, edge.z + dz)

                # out of bounds
                if (
                    pt.x < 0
                    or pt.y < 0
                    or pt.x >= world_slice.box.size.x
                    or pt.y >= world_slice.box.size.z
                ):
                    continue

                # don't smooth water tiles
                if water_map[pt.x][pt.y]:
                    continue

                if pt not in points:
                    points.add(pt)

    updated_heights = {}

    for x, z in points:
        key = x, z

        updated_heights[key] = average_neighbour_height(x, z, world_slice)

    for key, y in updated_heights.items():
        x, z = key
        set_height(x, y, z, world_slice, editor)

    editor.flushBuffer()  # this is needed to reload the world slice properly
    print("Reloading worldSlice")
    world_slice = editor.loadWorldSlice(build_rect)

    for district in districts:
        update_district_points(district, world_slice)
