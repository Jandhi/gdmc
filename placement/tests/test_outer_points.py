# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\placement\\tests')

# Actual file
from gdpc import Editor, Block
from gdpc.vector_tools import ivec3
from districts.generate_districts import generate_districts
from core.maps.water_map import get_water_map
from districts.tests.draw_districts import draw_districts
from core.utils.sets.find_outer_points import find_outer_and_inner_points

SEED = 752

editor = Editor(buffering=True, caching=True)

area = editor.getBuildArea()
editor.transform = (area.begin.x, 0, area.begin.z)

print("Loading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice loaded!")

water_map = get_water_map(world_slice)
districts, district_map = generate_districts(SEED, build_rect, world_slice, water_map)

draw_districts(districts, build_rect, district_map, water_map, world_slice, editor)

for district in districts:
    x = district.origin.x
    z = district.origin.z

    y = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][x][z] + 10
    editor.placeBlock((x, y, z), Block('sea_lantern'))

    outer, inner = find_outer_and_inner_points(district.points_2d, 2)

    for pt in outer:
        editor.placeBlock(ivec3(pt.x, world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][pt.x][pt.y], pt.y), Block('cobblestone'))