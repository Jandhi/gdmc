# Allows code to be run in root directory
import sys
import time

sys.path[0] = sys.path[0].removesuffix("\\tests\\placement")

# Actual file
from gdpc import Editor, Box
from gdpc.lookup import GRANULARS
from glm import ivec2

from grimoire.core.assets.load_assets import load_assets
from grimoire.core.maps import Map, get_build_map
from grimoire.core.noise.rng import RNG
from grimoire.core.utils.sets.find_outer_points import find_outer_and_inner_points
from grimoire.districts.district_painter import (
    replace_ground_smooth,
    plant_forest,
    replace_ground,
)
from grimoire.districts.generate_districts import generate_districts
from grimoire.districts.paint_palette import PaintPalette
from grimoire.districts.wall import (
    get_wall_points,
    order_wall_points,
    build_wall_standard_with_inner,
)
from grimoire.industries.biomes import snowy, rocky, desert, forest
from grimoire.industries.industry import get_district_biomes
from grimoire.palette import Palette
from grimoire.placement.city_blocks import add_city_blocks
from grimoire.terrain.forest import Forest
from grimoire.terrain.plateau import plateau
from grimoire.terrain.smooth_edges import smooth_edges
from grimoire.terrain.tree_cutter import log_trees


SEED = 0x4473
DO_TERRAFORMING = True  # Set this to true for the final iteration

editor = Editor(buffering=True, caching=True)
load_assets("grimoire/asset_data")

area = editor.getBuildArea()

# can't to do areas too large yet
if area.size.x > 1000:
    x = area.center.x - 400
    z = area.center.z - 400
    editor.setBuildArea(Box((x, 0, z), (350, area.size.y, 350)))

area = editor.getBuildArea()

editor.transform = (area.begin.x, 0, area.begin.z)

print("Loading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice loaded!")

log_trees(editor, build_rect, world_slice)

editor.flushBuffer()  # this is needed to reload the world slice properly
print("Reloading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice reloaded!")

map = Map(world_slice)
districts, district_map = generate_districts(SEED, build_rect, world_slice, map.water)
map.districts = district_map

styles = [
    "japanese",  # I think this is the strongest one, so probably used in most environments
    "viking",  # Pretty weak I think so we could avoid, but we can story it
    "desert",  # Decentish variety I think
    "dwarven",  # Little variety so probably save it for mountains
]

forest_counter = 0
desert_counter = 0
rocky_counter = 0
snowy_counter = 0
mountainous = False
is_snowy = False
is_desert = False
for district in districts:
    biomes_in_district = get_district_biomes(editor, district)
    for biome in biomes_in_district:
        if biome in forest:
            forest_counter += 1
        elif biome in desert:
            desert_counter += 1
        elif biome in rocky:
            mountainous = True
            rocky_counter += 1
        elif biome in snowy:
            snowy_counter += 1

if rocky_counter >= len(districts) // 2:
    mountainous = True
if snowy_counter >= len(districts) // 2:
    is_snowy = True
if desert_counter >= len(districts) // 2:
    is_desert = True
biome_counters = [forest_counter, desert_counter, rocky_counter]

if max(biome_counters) == forest_counter or max(biome_counters) not in [
    desert_counter,
    rocky_counter,
]:
    style = "japanese"
elif max(biome_counters) == desert_counter:
    style = "desert"
else:
    style = "dwarven"
# set up palettes
eligible_palettes = list(filter(lambda palette: style in palette.tags, Palette.all()))
rng = RNG(SEED, "palettes")

for district in districts:
    palettes = eligible_palettes.copy()

    for _ in range(min(3, len(eligible_palettes))):
        district.palettes.append(rng.pop(palettes))

# plateau stuff
if DO_TERRAFORMING:
    print("starting plateauing")
    for district in districts:
        if not district.is_urban:
            continue

        plateau(district, district_map, world_slice, editor, map.water)

    editor.flushBuffer()  # this is needed to reload the world slice properly
    print("Reloading worldSlice")
    world_slice = editor.loadWorldSlice(build_rect)
    map.world = world_slice

    smooth_edges(build_rect, districts, district_map, world_slice, editor, map.water)

    editor.flushBuffer()  # this is needed to reload the world slice properly
    print("Reloading worldSlice")
    world_slice = editor.loadWorldSlice(build_rect)
    map.world = world_slice
    map.correct_district_heights(districts)
# done

print("sleepy time to reduce http traffic")
time.sleep(10)  # to try to reduce http traffic, we'll do a little sleepy time

inner_points = []

for x in range(build_rect.size.x):
    for z in range(build_rect.size.y):
        district = district_map[x][z]

        if district is None:
            continue
        elif district.is_urban:
            inner_points.append(ivec2(x, z))

wall_points, wall_dict = get_wall_points(inner_points, world_slice)
wall_points_list = order_wall_points(wall_points, wall_dict)

rng = RNG(SEED)
palette = rng.choose(eligible_palettes)

build_map = get_build_map(world_slice, 20)

urban_road: PaintPalette = (
    PaintPalette.find("desert_road")
    if style == "desert"
    else PaintPalette.find("urban_road")
)
replace_ground_smooth(
    inner_points, urban_road.palette, rng, map.water, build_map, editor, world_slice
)

# draw_districts(districts, build_rect, district_map, map.water, world_slice, editor)

# for districts in districts:
#     x = districts.origin.x
#     z = districts.origin.z

#     y = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][x][z] + 10
#     editor.placeBlock((x, y, z), Block('sea_lantern'))

add_city_blocks(editor, districts, map, SEED, style=style, is_debug=False)

# WALL

# uncomment one of these to story one of the three wall types

for wall_points in wall_points_list:
    build_wall_standard_with_inner(
        wall_points,
        wall_dict,
        inner_points,
        editor,
        world_slice,
        map.water,
        rng,
        palette,
    )
# build_wall_palisade(wall_points, editor, map.world, map.water, rng, palette)
# build_wall_standard(wall_points, wall_dict, inner_points, editor, map.world, map.water, palette)

ignore_blocks = GRANULARS | {
    "minecraft:stone",
    "minecraft:copper_ore",
}

farmland: PaintPalette = PaintPalette.find("farmland")
forests = Forest.all()
crops = list(filter(lambda palette: "crops" in palette.tags, PaintPalette.all()))
rural_road: PaintPalette = PaintPalette.find("rural_road")

options = forests + crops

for district in districts:
    if not district.is_urban:
        if mountainous and not is_snowy or is_desert:
            choice_list = rng.choose([[None], [None], [None], [None]])
        elif is_snowy and not mountainous:
            choice_list = rng.choose([forests, [None], [None], [None]])
        else:
            choice_list = rng.choose([crops, forests, [None], [None]])
        choice = rng.choose(choice_list)

        outer_district_points, inner_district_points = find_outer_and_inner_points(
            district.points_2d, 4
        )
        if isinstance(choice, Forest):  # forest
            plant_forest(
                list(inner_district_points),
                choice,
                rng,
                map.water,
                build_map,
                editor,
                world_slice,
                ignore_blocks,
            )
        elif isinstance(choice, PaintPalette):  # crops
            replace_ground(
                list(inner_district_points),
                farmland.palette,
                rng,
                map.water,
                build_map,
                editor,
                world_slice,
                0,
                ignore_blocks,
            )
            replace_ground(
                list(inner_district_points),
                choice.palette,
                rng,
                map.water,
                build_map,
                editor,
                world_slice,
                1,
                ignore_blocks,
            )
            replace_ground(
                list(outer_district_points),
                rural_road.palette,
                rng,
                map.water,
                build_map,
                editor,
                world_slice,
            )
        else:
            continue

        time.sleep(5)  # to try to reduce http traffic, we'll do a little sleepy time
