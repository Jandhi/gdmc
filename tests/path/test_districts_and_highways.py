# Allows code to be run in root directory
import sys

sys.path[0] = sys.path[0].removesuffix("\\tests\\path")

# Actual file
from gdpc import Editor
from gdpc.vector_tools import ivec2, ivec3
from grimoire.districts.generate_districts import generate_districts
from grimoire.paths.route_highway import route_highway, fill_out_highway
from grimoire.paths.build_highway import build_highway
from grimoire.terrain.plateau import plateau
from grimoire.terrain.smooth_edges import smooth_edges
from grimoire.core.maps import Map

SEED = 243

editor = Editor(buffering=True, bufferLimit=1000, caching=True)

area = editor.getBuildArea()
editor.transform = (area.begin.x, 0, area.begin.z)

print("Loading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice loaded!")

editor.doBlockUpdates = False

player_pos = ivec2(area.size.x // 2, area.size.z // 2)


map = Map(world_slice)

water_map = map.water
districts, district_map = generate_districts(SEED, build_rect, world_slice, water_map)
map.districts = district_map

print("starting plateauing")
for district in districts:
    if not district.is_urban:
        continue

    plateau(district, district_map, world_slice, editor, water_map)

editor.flushBuffer()  # this is needed to reload the world slice properly
print("Reloading worldSlice")
world_slice = editor.loadWorldSlice(build_rect)

smooth_edges(build_rect, districts, district_map, world_slice, editor, water_map)

editor.flushBuffer()  # this is needed to reload the world slice properly
print("Reloading worldSlice")
world_slice = editor.loadWorldSlice(build_rect)

# draw_districts(districts, build_rect, district_map, water_map, world_slice, editor)

for district in districts:
    for other in district.adjacency:
        if other.id < district.id:
            continue

        point_a = ivec3(
            district.average().x,
            world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][district.average().x][
                district.average().z
            ],
            district.average().z,
        )

        point_b = ivec3(
            (other.average().x - other.average().x % 4) + (district.average().x % 4),
            0,
            (other.average().z - other.average().z % 4) + (district.average().z % 4),
        )
        point_b.y = world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][point_b.x][
            point_b.z
        ]

        highway = route_highway(point_a, point_b, map, editor, is_debug=True)
        highway = fill_out_highway(highway)
        build_highway(highway, editor, world_slice, map)

        world_slice = editor.loadWorldSlice(build_rect)
