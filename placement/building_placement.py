from gdpc.vector_tools import ivec2, ivec3, vec2
from core.maps.map import Map
from core.structures.legacy_directions import z_minus, z_plus, x_minus, x_plus, cardinal, get_ivec2
from core.structures.grid import Grid
from buildings.building_shape import BuildingShape
from core.maps.building_map import CITY_WALL, CITY_ROAD
from palette.palette import Palette
from buildings.building_plan import BuildingPlan
from gdpc import Editor, Block
from buildings.build_floor import build_floor
from buildings.roofs.roof_component import RoofComponent
from buildings.roofs.build_roof import build_roof
from buildings.walls.wall import Wall
from buildings.walls.build_walls import build_walls
from buildings.clear_interiors import clear_interiors
from core.noise.rng import RNG
from palette.palette_swap import fix_block_name
from buildings.rooms.furnish import furnish

offsets = {
    z_minus : [ivec2(0, 0), ivec2(-1, 0)],
    x_minus  : [ivec2(0, 0), ivec2(0, -1)],
    x_plus  : [ivec2(-1, -1), ivec2(-1, 0)],
    z_plus : [ivec2(-1, -1), ivec2(0, -1)],
}

door_points = {
    z_minus : vec2(0.5, 0),
    z_plus : vec2(0.5, 1),
    x_plus : vec2(1, 0.5),
    x_minus : vec2(0, 0.5),
}

WATER_THRESHOLD = 0.4 # above this threshold a house cannot be built
MAX_AVG_HEIGHT_DIFF = 4 

def place_building(editor : Editor, start_point : ivec2, map : Map, outside_direction : str, rng : RNG, style : str = 'japanese', urban_only = True):
    my_offsets = offsets[outside_direction]

    shapes : list[BuildingShape] = BuildingShape.all()

    shape_dict = {
        shape : len(shape.points) ** 2 + 2 for shape in shapes if shape.door_direction == outside_direction
    }

    while True:
        shape : BuildingShape = rng.pop_weighted(shape_dict)

        if shape is None:
            return
        
        if shape.door_direction != outside_direction:
            continue

        for offset in my_offsets:
            grid = Grid()
            origin = start_point + ivec2(offset.x * (grid.dimensions.x), offset.y * (grid.dimensions.z))

            # We have to find the proper height for the door to be at ground level
            door_point = ivec2(*door_points[outside_direction])
            door_point.x = (grid.dimensions.x // 2 + 1) if door_point.x == 0.5 else door_point.x * (grid.dimensions.x - 1)
            door_point.y = (grid.dimensions.z // 2 + 1) if door_point.y == 0.5 else door_point.y * (grid.dimensions.z - 1)

            road_point = nearest_road(origin + door_point, map)

            # Usually we should be able to find the nearest road, but otherwise we can default to the door height
            if road_point is None:
                road_point = origin + door_point

            grid.origin = ivec3(origin.x, map.height_at(road_point) - 1, origin.y)
            
            points = list(shape.get_points_2d(grid))
            is_free = True
            water_amt = 0
            total_height_diff = 0

            for point in points:
                # water check
                if map.water[point.x][point.y]:
                    water_amt += 1

                # freeness check
                if map.buildings[point.x][point.y] != None:
                    is_free = False
                    break

                # urban check
                if urban_only and (not map.districts[point.x][point.y] or not map.districts[point.x][point.y].is_urban):
                    is_free = False
                    break

                total_height_diff += abs(grid.origin.y - map.height_at(point))

            if WATER_THRESHOLD <= water_amt / len(points):
                is_free = False

            avg_height_diff = total_height_diff / len(points)
            if avg_height_diff >= MAX_AVG_HEIGHT_DIFF:
                is_free = False

            if not is_free:
                continue

            # build
            place(editor, shape, grid, rng, map, style)
            return
        
def nearest_road(start_point : ivec2, map : Map) -> ivec2:
    queue = [start_point]
    visited = set()
    limit = 100
    iterations = 0

    while len(queue) > 0:
        point = queue.pop(0)
        visited.add(point)
        iterations += 1

        if iterations > limit:
            return None

        if map.is_in_bounds2d(point) and (map.buildings[point.x][point.y] == CITY_ROAD or map.buildings[point.x][point.y] == CITY_WALL):
            return point
        
        for direction in cardinal:
            neighbour = point + get_ivec2(direction)
        
            if map.is_in_bounds2d(neighbour) and neighbour not in visited:
                queue.append(neighbour)
    
    return None

def place(editor : Editor, shape : BuildingShape, grid : Grid, rng : RNG, map : Map, style : str):
    district = map.districts[grid.origin.x][grid.origin.z]
    palette : Palette = rng.choose(district.palettes) if district else Palette.find('japanese_dark_blackstone')
    
    plan = BuildingPlan(shape.points, grid, palette)
    plan.cell_map[ivec3(0, 0, 0)].doors.append(shape.door_direction)

    for point in shape.get_points_2d(grid):
        map.buildings[point.x][point.y] = plan

    # Clear the area
    for point in shape.get_points(grid):
        editor.placeBlock(point, Block('air'))

    build_roof(plan, editor, [
        component for component in RoofComponent.all() if style in component.tags
    ], rng.next())

    clear_interiors(plan, editor)
    build_floor(plan, editor)

    walls = list(filter(lambda wall : style in wall.tags, Wall.all().copy()))

    build_walls(plan, editor, walls, rng)

    for point in shape.get_points_2d(grid):
        world_height = map.height_at(point)
        grid_height = grid.origin.y

        for y_coord in range(world_height, grid_height):
            editor.placeBlock(ivec3(point.x, y_coord, point.y), Block(fix_block_name(palette.primary_stone)))

    try:
        furnish([cell.position for cell in plan.cells], rng, grid, editor, palette, plan.cell_map)
    except Exception:
        pass # this is a last resort, this should not be used in the future