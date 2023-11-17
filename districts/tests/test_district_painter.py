# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\districts\\tests')

from gdpc import Editor, Block
from gdpc.vector_tools import ivec2
from districts.generate_districts import generate_districts
from core.maps.water_map import get_water_map
from core.maps.build_map import get_build_map
from core.noise.rng import RNG
from core.noise.random import choose_weighted
from districts.district_painter import plant_forest
from core.assets.load_assets import load_assets
from districts.paint_palette import PaintPalette
from terrain.forest import Forest

SEED = 2

editor = Editor(buffering=True, caching=True)

area = editor.getBuildArea()
print(area)
editor.transform = (area.begin.x, 0, area.begin.z)

print("Loading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice loaded!")


water_map = get_water_map(world_slice)
build_map = get_build_map(world_slice)
districts, district_map = generate_districts(SEED, build_rect, world_slice, water_map)

#draw_districts(districts, build_rect, district_map, water_map, world_slice, editor)
load_assets('assets')

def place_crop(points: list[ivec2], block_dict: dict[any,int], rng, water_map):
    for point in points:
        if water_map[point.x][point.y] == False:
            block = choose_weighted(rng.value(), block_dict)
            y = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][point.x][point.y]
            editor.placeBlock((point.x, y  , point.y), Block(block))


urban_points = []
rural_points = []
all_points = []

for x in range(build_rect.size.x):
    for z in range(build_rect.size.y):
        district = district_map[x][z]

        if district is None:
            continue
        #elif district.is_urban:
        #    urban_points.append(ivec2(x,z))
        else:
            #rural_points.append(ivec2(x,z))
            all_points.append(ivec2(x,z))

rng = RNG(SEED)


test_farm = {

    'wheat[age=1]' : 1,
    'wheat[age=2]' : 1,
    'wheat[age=3]' : 1,
    'wheat[age=4]' : 1,
    'wheat[age=5]' : 1,
    'wheat[age=6]' : 1,
    'wheat[age=7]' : 1
}

ignore_blocks = [
    'minecraft:sand',
    'minecraft:gravel',
    'minecraft:stone',
    'minecraft:copper_ore'
]

test_blocks = {
    "farmland[moisture=7]": 1
}

test_blocks2 = {
    'beetroots[age=0]' : 1,
    'beetroots[age=1]' : 1,
    'beetroots[age=2]' : 2,
    'beetroots[age=3]' : 2
}



baobab = {
    'small_baobab': 1
}

test : PaintPalette = PaintPalette.find('farmland')
test2 : PaintPalette = PaintPalette.find('carrot')
forest : Forest = Forest.find('mixed_forest')
#replace_ground(all_points, test_blocks2, rng, water_map, build_map, editor, world_slice)
#replace_ground(all_points, test.palette, rng, water_map, build_map, editor, world_slice, 0, ignore_blocks)
#replace_ground(all_points, test2.palette, rng, water_map, build_map, editor, world_slice, 1, ignore_blocks)
#replace_ground(urban_points, urban_road, rng, water_map, build_map, editor, world_slice)
#replace_ground_smooth(urban_points, urban, rng, water_map, build_map, editor, world_slice)
plant_forest(all_points, forest, rng, water_map, build_map, editor, world_slice, ignore_blocks)