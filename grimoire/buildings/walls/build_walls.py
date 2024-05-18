from ..building_plan import BuildingPlan
from ..legacycell import LegacyCell
from ...core.structures.legacy_directions import CARDINAL, LegacyDirection, UP
from gdpc.editor import Editor
from .wall import Wall, LOWER, UPPER
from ...core.noise.rng import RNG
from ...core.structures.grid import Grid

NOT_ROOF = "not_roof"
ONLY_ROOF = "only_roof"


def build_walls(plan: BuildingPlan, editor: Editor, walls: list[Wall], rng: RNG):
    for cell in plan.cells:
        for direction in CARDINAL:
            if not cell.has_neighbour(direction):
                build_wall(cell, direction, editor, walls, rng)


def build_wall(
    cell: LegacyCell,
    direction: LegacyDirection,
    editor: Editor,
    walls: list[Wall],
    rng: RNG,
):
    has_door = cell.has_door(direction)

    def wall_is_eligible(wall: Wall):
        if wall.has_door != has_door:
            return False

        return bool(
            (cell.position.y != 0 or wall.has_position(LOWER))
            and (cell.position.y <= 0 or wall.has_position(UPPER))
            and (cell.has_neighbour(UP) or NOT_ROOF not in wall.tags)
            and (not cell.has_neighbour(UP) or ONLY_ROOF not in wall.tags)
        )

    eligible_walls: list[Wall] = list(filter(wall_is_eligible, walls))

    weighted_walls = {
        wall: wall.weight if wall.weight > 0 else 100 for wall in eligible_walls
    }

    wall: Wall = rng.choose_weighted(weighted_walls)
    grid: Grid = cell.plan.grid

    if wall is None:
        print("Could not find suitable wall, skipped")
        return

    grid.build(editor, wall, cell.plan.palette, cell.position, direction)
