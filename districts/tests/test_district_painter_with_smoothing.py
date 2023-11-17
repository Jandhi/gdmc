# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\districts\\tests')

from gdpc import Editor
from gdpc.vector_tools import ivec2
from districts.generate_districts import generate_districts
from terrain.smooth_edges import smooth_edges
from core.maps.water_map import get_water_map
from core.maps.build_map import get_build_map
from terrain.plateau import plateau
from core.noise.rng import RNG

from districts.district_painter import plant_forest, replace_ground_smooth

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

print('starting plateauing')
for district in districts:
    #if not district.is_urban:
        #continue

    plateau(district, district_map, world_slice, editor, water_map)

editor.flushBuffer() # this is needed to reload the world slice properly
print('Reloading worldSlice')
world_slice = editor.loadWorldSlice(build_rect)

smooth_edges(build_rect, districts, district_map, world_slice, editor, water_map)

editor.flushBuffer() # this is needed to reload the world slice properly
print('Reloading worldSlice')
world_slice = editor.loadWorldSlice(build_rect)

#draw_districts(districts, build_rect, district_map, water_map, world_slice, editor)

urban_points = []
rural_points = []

for x in range(build_rect.size.x):
    for z in range(build_rect.size.y):
        district = district_map[x][z]

        if district is None:
            continue
        elif district.is_urban:
            urban_points.append(ivec2(x,z))
        else:
            rural_points.append(ivec2(x,z))

rng = RNG(SEED)

test_blocks = {
    f'farmland[moisture=6]': 1
}

urban_road = {
    'stone': 3,
    'cobblestone' : 2,
    'stone_bricks' : 8,
    'andesite' : 3,
    'gravel' : 1
}

test_farm = {

    f'wheat[age=7]' : 1
}

urban = {
    'slabs' : {'stone_slab': 3,'cobblestone_slab' : 2,'stone_brick_slab' : 8,'andesite_slab' : 4},
    'blocks' : {'stone': 3,'cobblestone' : 2,'stone_bricks' : 8,'andesite' : 3,'gravel' : 1},
    'stairs' : {'stone_stairs': 3,'cobblestone_stairs' : 2,'stone_brick_stairs' : 8,'andesite_stairs' : 4}
}

oak_forest = {
    'mega_oak': 1,
    'large_oak': 3,
    'medium_oak': 4,
    'small_oak': 3
}

ignore_blocks = [
    'minecraft:sand',
    'minecraft:gravel'
]

replace_ground_smooth(urban_points, urban, rng, water_map, build_map, editor, world_slice)
plant_forest(rural_points, oak_forest, rng, water_map, build_map, editor, world_slice, ignore_blocks)