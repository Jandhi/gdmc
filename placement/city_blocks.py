from districts.district import District
from gdpc import Editor, Block
from gdpc.vector_tools import ivec2, ivec3, distance2
from core.utils.sets.set_operations import calculate_stretch, find_edges, find_outer_direction
from core.utils.sets.find_outer_points import find_outer_and_inner_points
from core.noise.rng import RNG
from core.structures.legacy_directions import cardinal, get_ivec2, to_text
from core.utils.bounds import is_in_bounds2d
from core.utils.vectors import point_3d, y_ivec3
from core.maps.map import Map
from core.maps.building_map import CITY_WALL, CITY_ROAD
from placement.building_placement import place_building

MAXIMUM_SIZE = 2000

UNSPLITTABLE_SIZE = 100 
MAXIMUM_STRETCH_RATIO = 5
EDGE_THICKNESS = 1
DESIRED_BLOCK_SIZE = 500
MINIMUM_BLOCK_SZE = 100

def block_is_admissible(points : set[ivec2]) -> bool:
    # We will automatically pass this as it should not be split again
    if len(points) <= UNSPLITTABLE_SIZE:
        return True
    
    if len(points) > MAXIMUM_SIZE:
        return False
    
    stretch = calculate_stretch(points)

    if stretch.x / stretch.y > MAXIMUM_STRETCH_RATIO or stretch.y / stretch.x > MAXIMUM_STRETCH_RATIO:
        return False
    
    return True

def generate_bubbles(rng : RNG, districts : list[District], map : Map, desired_block_size = 1200, minimum_point_distance = 15) -> list[ivec2]:
    points = []

    for district in districts:
        if not district.is_urban:
            continue

        desired_point_amount = district.area // desired_block_size
        district_points_generated = 0
        trials = 0
        max_trials = 2 * desired_point_amount
        district_points = list(district.points_2d)

        while trials < max_trials and district_points_generated < desired_point_amount:
            trials += 1
            point = rng.pop(district_points) # choose random point in district

            if any(distance2(point, other) < minimum_point_distance for other in points):
                continue

            if map.buildings[point.x][point.y] == CITY_WALL:
                continue
            
            district_points_generated += 1
            points.append(point)
    
    return points

def bubble_out(bubbles : list[ivec2], map : Map) -> tuple[list[set[ivec2]], list[list[int]], dict[int, dict[int, int]]]:
    block_index_map = [[None for _ in range(len(map.districts[0]))] for _ in range(len(map.districts))]
    blocks = [set() for _ in bubbles]
    num_blocks = len(blocks)
    block_adjacency = {
        block : {other : 0 for other in range(num_blocks)} for block in range(num_blocks)
    }

    for i, bubble in enumerate(bubbles):
        blocks[i].add(bubble)
        block_index_map[bubble.x][bubble.y] = i

    queue = [bubble for bubble in bubbles]

    def is_eligible(vec : ivec2):
        district = map.districts[vec.x][vec.y]

        if map.buildings[vec.x][vec.y] == CITY_WALL:
            return False
        
        if map.water[vec.x][vec.y]:
            return False

        return district != None and district.is_urban

    while len(queue) > 0:
        point = queue.pop(0)
        block_index = block_index_map[point.x][point.y]
        block : set[ivec3] = blocks[block_index]

        for direction in cardinal:
            neighbour = point + get_ivec2(direction)

            if not is_in_bounds2d(neighbour, map.world):
                continue

            point_y = map.world.heightmaps['MOTION_BLOCKING_NO_LEAVES'][point.x][point.y]
            neighbour_y = map.world.heightmaps['MOTION_BLOCKING_NO_LEAVES'][neighbour.x][neighbour.y]

            if abs(point_y - neighbour_y) > 1:
                continue

            neighbour_block_index = block_index_map[neighbour.x][neighbour.y]
            if neighbour_block_index != None:
                block_adjacency[block_index][neighbour_block_index] += 1
                block_adjacency[neighbour_block_index][block_index] += 1
                continue

            if not is_eligible(neighbour):
                continue

            block_index_map[neighbour.x][neighbour.y] = block_index
            block.add(neighbour)
            queue.append(neighbour)
    
    return blocks, block_index_map, block_adjacency

def merge_small_blocks(blocks : list[set[ivec2]], block_map : list[list[int]], block_adjacency : dict[int, dict[int, int]]):    
    for index, block in enumerate(blocks):
        
        if len(block) > MINIMUM_BLOCK_SZE: 
            continue
        
        best_neighbour = None
        best_index = 0
        best_adjacency = -1

        for other_index, adjacency in block_adjacency[index].items():
            if adjacency > best_adjacency:
                best_neighbour = blocks[other_index]
                best_index = other_index
        
        # couldn't find someone to merge with
        if best_neighbour is None:
            continue

        for point in block:
            best_neighbour.add(point)
            block_map[point.x][point.y] = best_index

        block.clear()

    return blocks, block_map

def place_buildings(editor : Editor, block : set[ivec2], map : Map, rng : RNG, style='japanese', is_debug = False):
    edges = find_edges(block)

    for edge in edges:
        build_dir = find_outer_direction(edge, block, rng.chance(1, 2))

        if is_debug:
            editor.placeBlock(point_3d(edge, map.world) + y_ivec3(-1), Block('cobblestone_stairs', {'facing' : to_text(build_dir)}))
        
        place_building(editor, edge, map, build_dir, rng, style)

def add_city_blocks(editor : Editor, districts : list[District], map : Map, seed : int, style = 'japanese', is_debug=False):
    rng = RNG(seed, 'add_city_blocks')

    urban_area : set[ivec2] = set()
    for district in districts:
        if district.is_urban:
            urban_area |= district.points_2d

    outer_urban_area, inner_urban_area = find_outer_and_inner_points(urban_area, 3)

    for point in outer_urban_area:
        map.buildings[point.x][point.y] = CITY_WALL

    bubbles = generate_bubbles(rng, districts, map)
    blocks, block_map, block_adjacency = bubble_out(bubbles, map)
    blocks, block_map = merge_small_blocks(blocks, block_map, block_adjacency)

    inners = []

    for i, block in enumerate(blocks):
        if len(block) < MINIMUM_BLOCK_SZE:
            continue

        outer, inner = find_outer_and_inner_points(block, EDGE_THICKNESS)

        for point in outer:
            map.buildings[point.x][point.y] = CITY_ROAD

        if is_debug:
            for point in outer | outer_urban_area:
                editor.placeBlock(ivec3(point.x, map.world.heightmaps['MOTION_BLOCKING_NO_LEAVES'][point.x][point.y] - 1, point.y), Block('cobblestone'))

        block_rng = RNG(seed, f'block {i}')
        inners.append(inner)

    # Has to be done after all inners are found
    for i, block in enumerate(blocks):
        if i >= len(inners):
            continue

        place_buildings(editor, inners[i], map, block_rng, style, is_debug)

        