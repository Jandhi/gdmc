from gdpc.editor import Editor
from glm import ivec3

from ...core.noise.global_seed import GlobalSeed
from ...core.noise.rng import RNG
from ...core.structures.grid import Grid
from ...core.structures.legacy_directions import LegacyDirection, cardinal, up
from ...core.styling.materials.dithering import DitheringPattern
from ...core.styling.materials.gradient import Gradient, GradientAxis, PerlinSettings
from ...core.styling.materials.material import MaterialParameterFunction
from ..building_plan import BuildingPlan
from ..legacycell import LegacyCell
from .wall import LOWER, UPPER, Wall

NOT_ROOF = "not_roof"
ONLY_ROOF = "only_roof"


def build_walls(plan: BuildingPlan, editor: Editor, walls: list[Wall], rng: RNG):

    shade_gradient = Gradient(
        seed=GlobalSeed.get(),
        perlin_settings=PerlinSettings(
            base_octaves=27, noise_layers=6, add_ratio=1.7, strength=0.2
        ),
    ).with_axis(
        GradientAxis.y(plan.grid.origin.y, plan.grid.origin.y + plan.grid.height * 2)
    )

    material_params_func = MaterialParameterFunction(
        shade_func=lambda point: shade_gradient.calculate_value(point),
        age_func=lambda point: 0,
        moisture_func=lambda point: 0,
        dithering_pattern=DitheringPattern.RANDOM,
    )

    for cell in plan.cells:
        for direction in cardinal:
            if not cell.has_neighbour(direction):
                build_wall(
                    cell,
                    direction,
                    editor,
                    walls,
                    rng,
                    material_params_func=material_params_func,
                )


def build_wall(
    cell: LegacyCell,
    direction: LegacyDirection,
    editor: Editor,
    walls: list[Wall],
    rng: RNG,
    material_params_func: MaterialParameterFunction | None = None,
):
    has_door = cell.has_door(direction)

    def wall_is_eligible(wall: Wall):
        if wall.has_door != has_door:
            return False

        return bool(
            (cell.position.y != 0 or wall.has_position(LOWER))
            and (cell.position.y <= 0 or wall.has_position(UPPER))
            and (cell.has_neighbour(up) or NOT_ROOF not in wall.tags)
            and (not cell.has_neighbour(up) or ONLY_ROOF not in wall.tags)
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

    grid.build(
        editor,
        wall,
        cell.plan.palette,
        cell.position,
        direction,
        material_params_func=material_params_func,
    )
