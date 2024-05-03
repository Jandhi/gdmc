from ..districts.district import District
from gdpc import Editor, WorldSlice
from gdpc.vector_tools import ivec2, ivec3
from ..terrain.set_height import set_height
from ..core.utils.bounds import is_in_bounds2d


def smooth(
    district: District,
    district_map: list[list[District]],
    world_slice: WorldSlice,
    editor: Editor,
    water_map: list[list[bool]],
):
    print(f"Smoothing {district}")
    updated_heights = {}

    for x, _, z in district.points:
        key = x, z

        # we don't want to flatten water tiles
        if water_map[x][z]:
            continue

        updated_heights[key] = average_neighbour_height(x, z, world_slice)

    for key, y in updated_heights.items():
        x, z = key
        set_height(x, y, z, world_slice, editor)


RANGE = 10
NEIGHBOURS = [
    (x, z) for x in range(-RANGE, RANGE + 1) for z in range(-RANGE, RANGE + 1)
]


def average_neighbour_height(x: int, z: int, world_slice: WorldSlice) -> int:
    height_sum = 0
    total_weight = 0

    for dx, dz in NEIGHBOURS:
        if not is_in_bounds2d(ivec2(x + dx, z + dz), world_slice):
            continue

        distance = abs(dx) + abs(dz)
        weight = 0.8**distance
        height = world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x + dx][z + dz]
        height_sum += height * weight
        total_weight += weight

    return round(height_sum / total_weight)


# updates the points set of a districts to be correct
def update_district_points(district: District, world_slice: WorldSlice):
    district.points.clear()

    for x, z in district.points_2d:
        y = world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x][z]
        point = ivec3(x, y, z)
        district.points.add(point)
