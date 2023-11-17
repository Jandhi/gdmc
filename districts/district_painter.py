from gdpc import Editor, Block, WorldSlice
from gdpc.vector_tools import ivec2, ivec3
from core.noise.rng import RNG
from core.noise.random import choose_weighted, shuffle
from terrain.tree import generate_tree
from core.structures.legacy_directions import cardinal, get_ivec2, to_text
from terrain.forest import Forest
import time

#gives the ability to provide a list of blocks upon which not to place
def replace_ground(points: list[ivec2], block_dict: dict[any,int], rng: RNG, water_map: list[list[bool]], build_map: list[list[bool]], editor: Editor, world_slice: WorldSlice, height_offset: int = 0, ignore_blocks: list = [], ignore_water: bool = False):
    counter = 0
    for point in points:
        counter += 1

        if counter % 1000 == 0:
            time.sleep(5)

        if (ignore_water or water_map[point.x][point.y] == False) and build_map[point.x][point.y] == False:
            y = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][point.x][point.y]
            if editor.getBlock(ivec3(point.x, y - 1, point.y)).id not in ignore_blocks:
                block = choose_weighted(rng.value(), block_dict)
                editor.placeBlock((point.x, y - 1 + height_offset, point.y), Block(block))

#requires the block dict to have 3 dicts inside, blocks, slabs, stairs
def replace_ground_smooth(points: list[ivec2], block_dict: dict[any,int], rng: RNG, water_map: list[list[bool]], build_map: list[list[bool]], editor: Editor, world_slice: WorldSlice, height_offset: int = 0, ignore_blocks: list = [], ignore_water: bool = False):
    counter = 0
    for point in points:
        counter += 1

        if counter % 1000 == 0:
            time.sleep(5)

        if (ignore_water or water_map[point.x][point.y] == False) and build_map[point.x][point.y] == False:
            y = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][point.x][point.y]
            if editor.getBlock(ivec3(point.x, y - 1, point.y)).id not in ignore_blocks:
                #decide on slab/stair/block
                block = None
                y_in_dir = {}

                for direction in cardinal:
                    delta = get_ivec2(direction)
                    neighbour = point + delta
                    opposite_neighbour = point - delta

                    if neighbour in points:
                        y_in_dir[direction] = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][neighbour.x][neighbour.y]

                    if world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][neighbour.x][neighbour.y] == y + 1 and world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][opposite_neighbour.x][opposite_neighbour.y] == y - 1:
                        block = choose_weighted(rng.value(), block_dict['stairs']) + f'[facing={to_text(direction)}]'
                        break
                    
                if all(y_in_dir[direction] <= y for direction in y_in_dir) and any(y_in_dir[direction] < y for direction in y_in_dir):
                    block = choose_weighted(rng.value(), block_dict['slabs'])

                if block == None:
                    block = choose_weighted(rng.value(), block_dict['blocks'])
                
                editor.placeBlock((point.x, y - 1 + height_offset, point.y), Block(block))


def plant_forest(points: list[ivec2], forest: Forest, rng: RNG, water_map: list[list[bool]], build_map: list[list[bool]], editor: Editor, world_slice: WorldSlice, ignore_blocks: list = [], ignore_water: bool = False):
    points = shuffle(rng.value(), points)
    for point in points:
        if (ignore_water or water_map[point.x][point.y] == False) and build_map[point.x][point.y] == False:
            y = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][point.x][point.y]
            if editor.getBlock(ivec3(point.x, y - 1, point.y)).id not in ignore_blocks:
                tree_type = choose_weighted(rng.value(), forest.tree_dict)
                generate_tree(tree_type, ivec3(point.x, y, point.y), editor, forest.tree_palette[tree_type])
                for a in range(point.x -forest.tree_density+1, point.x+forest.tree_density):
                    for b in range(point.y -forest.tree_density+1, point.y+forest.tree_density):
                        build_map[a][b] = True
