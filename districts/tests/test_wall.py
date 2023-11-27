# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\districts\\tests')

from gdpc import Editor, Block
from gdpc.vector_tools import ivec2
from districts.generate_districts import generate_districts
from core.utils.geometry import get_outer_points
from districts.wall import order_wall_points, build_wall_standard_with_inner
from core.maps.water_map import get_water_map
from core.noise.rng import RNG
from palette.palette import Palette
from core.assets.load_assets import load_assets

SEED = 7

editor = Editor(buffering=True, caching=True)
#editor.doBlockUpdates(value = False)
load_assets('assets')

area = editor.getBuildArea()
editor.transform = (area.begin.x, 0, area.begin.z)

print("Loading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice loaded!")


water_map = get_water_map(world_slice)
districts, district_map = generate_districts(SEED, build_rect, world_slice, water_map)

#draw_districts(districts, build_rect, district_map, water_map, world_slice, editor)

def place_at_ground(x, z, block_name):
    y = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][x][z]
    editor.placeBlock((x, y - 1, z), Block(block_name))

def replace_ground(points: list[ivec2], block_dict: dict[any,int], rng : RNG, water_map):
    for point in points:
        if water_map[point.x][point.y] == False:
            block = rng.choose_weighted(block_dict)
            place_at_ground(point.x, point.y, block)

test_blocks = {
    'stone': 3,
    'cobblestone' : 2,
    'stone_bricks' : 8,
    'andesite' : 3,
    'gravel' : 1
}

test_blocks_dirt = {
    'rooted_dirt': 3,
    'dirt' : 4,
    'podzol' : 2,
    'coarse_dirt' : 3,
}

inner_points = []

for x in range(build_rect.size.x):
    for z in range(build_rect.size.y):
        district = district_map[x][z]

        if district is None:
            continue
        elif district.is_urban:
            inner_points.append(ivec2(x,z))

wall_points, wall_dict = get_outer_points(inner_points, world_slice)
wall_points_list = order_wall_points(wall_points, wall_dict)

rng = RNG(SEED)
palette = Palette.find('japanese_dark_blackstone')

#uncomment one of these to tests one of the three wall types

for wall_points in wall_points_list:
    build_wall_standard_with_inner(wall_points, wall_dict, inner_points, editor, world_slice, water_map, rng, palette)
#build_wall_palisade(wall_points, editor, world_slice, water_map, rng, palette)
#build_wall_standard(wall_points, wall_dict, inner_points, editor, world_slice, water_map, palette)

#can use either test_blocks for more urban or test_blocks_dirt for dirty ground
replace_ground(inner_points, test_blocks_dirt, rng, water_map)