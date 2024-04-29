import contextlib
from gdpc.vector_tools import ivec2, ivec3, vec2
from grimoire.core.maps.map import Map
from grimoire.core.structures.legacy_directions import (
    z_minus,
    z_plus,
    x_minus,
    x_plus,
    cardinal,
    get_ivec2,
    LegacyDirection,
)
from grimoire.core.structures.grid import Grid
from grimoire.buildings.building_shape import BuildingShape
from grimoire.core.maps.building_map import CITY_WALL, CITY_ROAD
from grimoire.palette.palette import Palette
from grimoire.buildings.building_plan import BuildingPlan
from gdpc import Editor, Block
from grimoire.buildings.build_floor import build_floor
from grimoire.buildings.roofs.roof_component import RoofComponent
from grimoire.buildings.roofs.build_roof import build_roof
from grimoire.buildings.walls.wall import Wall
from grimoire.buildings.walls.build_walls import build_walls
from grimoire.buildings.clear_interiors import clear_interiors
from grimoire.core.noise.rng import RNG
from grimoire.palette.palette_swap import fix_block_name
from grimoire.buildings.rooms.furnish import furnish

offsets = {
    z_minus: [ivec2(0, 0), ivec2(-1, 0)],
    x_minus: [ivec2(0, 0), ivec2(0, -1)],
    x_plus: [ivec2(-1, -1), ivec2(-1, 0)],
    z_plus: [ivec2(-1, -1), ivec2(0, -1)],
}

door_points = {
    z_minus: vec2(0.5, 0),
    z_plus: vec2(0.5, 1),
    x_plus: vec2(1, 0.5),
    x_minus: vec2(0, 0.5),
}

WATER_THRESHOLD = 0.4  # above this threshold a house cannot be built
MAX_AVG_HEIGHT_DIFF = 4


# Attempts to place a building at a point
# returns True on success
def place_building(
    editor: Editor,
    start_point: ivec2,
    map: Map,
    outside_direction: str,
    rng: RNG,
    style: str = "japanese",
    urban_only=True,
) -> bool:
    # A building can always be placed with the door to the left or right of the original spot
    my_offsets = offsets[outside_direction]

    shapes: list[BuildingShape] = BuildingShape.all()

    # We increase the weight of larger buildings exponentially since they are much harder to place
    def building_shape_weight(shape: BuildingShape):
        return len(shape.points) ** 2 + 2

    weighted_shape_dict = {
        shape: building_shape_weight(shape)
        for shape in shapes
        if shape.door_direction == outside_direction
    }

    # iterate over shapes randomly by weight
    while True:
        shape: BuildingShape = rng.pop_weighted(weighted_shape_dict)

        if shape is None:
            return False

        if shape.door_direction != outside_direction:
            continue

        for offset in my_offsets:
            success = attempt_building_placement_at_offset(
                editor,
                rng,
                map,
                start_point,
                offset,
                outside_direction,
                shape,
                style,
                urban_only,
            )

            if success:
                return True


# Attempts to place building, returns success status
def attempt_building_placement_at_offset(
    editor: Editor,
    rng: RNG,
    map: Map,
    start_point: ivec2,
    offset: ivec2,
    outside_direction: LegacyDirection,
    shape: BuildingShape,
    style: str,
    urban_only: bool,
) -> bool:
    grid = Grid()
    origin = start_point + ivec2(
        offset.x * grid.dimensions.x, offset.y * grid.dimensions.z
    )

    # We have to find the proper height for the door to be at ground level
    door_point = ivec2(*door_points[outside_direction])
    door_point.x = (
        (grid.dimensions.x // 2 + 1)
        if door_point.x == 0.5
        else door_point.x * (grid.dimensions.x - 1)
    )
    door_point.y = (
        (grid.dimensions.z // 2 + 1)
        if door_point.y == 0.5
        else door_point.y * (grid.dimensions.z - 1)
    )

    road_point = nearest_road(origin + door_point, map)

    # Usually we should be able to find the nearest road, but otherwise we can default to the door height
    if road_point is None:
        road_point = origin + door_point

    grid.origin = ivec3(origin.x, map.height_at(road_point) - 1, origin.y)

    if not can_place_shape(shape, grid, map, urban_only):
        return False

    # build
    place(editor, shape, grid, rng, map, style)
    return True


def can_place_shape(shape: BuildingShape, grid: Grid, map: Map, urban_only: bool):
    points = list(shape.get_points_2d(grid))
    water_amt = 0
    total_height_diff = 0

    for point in points:
        # water check
        if map.water[point.x][point.y]:
            water_amt += 1

        # freeness check
        if map.buildings[point.x][point.y] is not None:
            return False

        # urban check
        if urban_only and (
            not map.districts[point.x][point.y]
            or not map.districts[point.x][point.y].is_urban
        ):
            return False

        total_height_diff += abs(grid.origin.y - map.height_at(point))

    if WATER_THRESHOLD <= water_amt / len(points):
        return False

    avg_height_diff = total_height_diff / len(points)
    if avg_height_diff >= MAX_AVG_HEIGHT_DIFF:
        return False

    return True


def nearest_road(start_point: ivec2, map: Map) -> ivec2 | None:
    queue = [start_point]
    visited = set()
    limit = 100
    iterations = 0

    while queue:
        point = queue.pop(0)
        visited.add(point)
        iterations += 1

        if iterations > limit:
            return None

        if map.is_in_bounds2d(point) and map.buildings[point.x][point.y] in [
            CITY_ROAD,
            CITY_WALL,
        ]:
            return point

        for direction in cardinal:
            neighbour = point + get_ivec2(direction)

            if map.is_in_bounds2d(neighbour) and neighbour not in visited:
                queue.append(neighbour)

    return None


def place(
    editor: Editor, shape: BuildingShape, grid: Grid, rng: RNG, map: Map, style: str
):
    district = map.districts[grid.origin.x][grid.origin.z]
    palette: Palette = (
        rng.choose(district.palettes)
        if district
        else Palette.find("japanese_dark_blackstone")
    )

    plan = BuildingPlan(shape.points, grid, palette)
    plan.cell_map[ivec3(0, 0, 0)].doors.append(shape.door_direction)

    for point in shape.get_points_2d(grid):
        map.buildings[point.x][point.y] = plan

    # Clear the area
    for point in shape.get_points(grid):
        editor.placeBlock(point, Block("air"))

    build_roof(
        plan,
        editor,
        [component for component in RoofComponent.all() if style in component.tags],
        rng.next(),
    )

    clear_interiors(plan, editor)
    build_floor(plan, editor)

    walls = list(filter(lambda wall: style in wall.tags, Wall.all().copy()))

    build_walls(plan, editor, walls, rng)

    for point in shape.get_points_2d(grid):
        world_height = map.height_at(point)
        grid_height = grid.origin.y

        for y_coord in range(world_height, grid_height):
            editor.placeBlock(
                ivec3(point.x, y_coord, point.y),
                Block(fix_block_name(palette.primary_stone)),
            )

    # FIXME: this suppression is a last resort, and should not be used in the future
    with contextlib.suppress(Exception):
        furnish(
            [cell.position for cell in plan.cells],
            rng,
            grid,
            editor,
            palette,
            plan.cell_map,
        )
