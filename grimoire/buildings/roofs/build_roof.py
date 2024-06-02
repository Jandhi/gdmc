from gdpc import Editor
from gdpc.vector_tools import ivec3
from .roof_component import RoofComponent, CORNER, INNER, SIDE
from ..building_plan import BuildingPlan
from ...core.noise.global_seed import GlobalSeed
from ...core.structures.grid import Grid
from ...core.structures.legacy_directions import north, south, east, west, up
from ...core.styling.materials.dithering import DitheringPattern
from ...core.styling.materials.gradient import Gradient, GradientAxis, PerlinSettings
from ...core.styling.materials.material import MaterialParameterFunction
from ...core.utils.vectors import y_ivec3
from ...core.structures.nbt.build_nbt import build_nbt_legacy, build_nbt
from ...core.structures.transformation import Transformation
from ...core.noise.rng import RNG


def build_roof(
    plan: BuildingPlan, editor: Editor, roofComponents: list[RoofComponent], seed: int
):
    grid: Grid = plan.grid
    rng = RNG(seed, "build_roof")

    shade_gradient = Gradient(
        seed=rng.next(),
        perlin_settings=PerlinSettings(
            base_octaves=27, noise_layers=6, add_ratio=1.7, strength=0.2
        ),
    ).with_axis(
        GradientAxis.y(
            plan.grid.origin.y + plan.grid.height - 2,
            plan.grid.origin.y + plan.grid.height * 2,
        )
    )

    material_params_func = MaterialParameterFunction(
        shade_func=lambda point: shade_gradient.calculate_value(point),
        age_func=lambda point: 0,
        moisture_func=lambda point: 0,
        dithering_pattern=DitheringPattern.RANDOM,
    )

    def roof_is_shape(shape: str):
        return lambda roof: roof.shape == shape

    corners = list(filter(roof_is_shape(CORNER), roofComponents))
    inners = list(filter(roof_is_shape(INNER), roofComponents))
    sides = list(filter(roof_is_shape(SIDE), roofComponents))

    corner = rng.choose(corners)
    inner = rng.choose(inners)
    side = rng.choose(sides)

    # northwest
    for cell in plan.cells:
        if cell.has_neighbour(up):
            continue

        coords = grid.grid_to_local(cell.position + y_ivec3(1)) + grid.origin

        # northwest
        if cell.has_neighbour(north) and cell.has_neighbour(west):
            build_nbt(
                editor,
                inner,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(0, 0, 0),
                ),
                material_params_func=material_params_func,
            )
        elif not cell.has_neighbour(north) and not cell.has_neighbour(west):
            build_nbt(
                editor,
                corner,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(0, 0, 0),
                ),
                material_params_func=material_params_func,
            )
        elif cell.has_neighbour(north) and not cell.has_neighbour(west):
            build_nbt(
                editor,
                side,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(0, 0, grid.depth // 2),
                    mirror=(False, False, True),
                ),
                material_params_func=material_params_func,
            )
        else:
            build_nbt(
                editor,
                side,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(grid.width // 2, 0, 0),
                    mirror=(False, False, True),
                    diagonal_mirror=True,
                ),
                material_params_func=material_params_func,
            )

        # northeast
        if cell.has_neighbour(north) and cell.has_neighbour(east):
            build_nbt(
                editor,
                inner,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(grid.width - 1, 0, 0),
                    mirror=(True, False, False),
                ),
                material_params_func=material_params_func,
            )
        elif not cell.has_neighbour(north) and not cell.has_neighbour(east):
            build_nbt(
                editor,
                corner,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(grid.width - 1, 0, 0),
                    mirror=(True, False, False),
                ),
                material_params_func=material_params_func,
            )
        elif cell.has_neighbour(north) and not cell.has_neighbour(east):
            build_nbt(
                editor,
                side,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(grid.width - 1, 0, grid.depth // 2),
                    mirror=(True, False, True),
                ),
                material_params_func=material_params_func,
            )
        else:
            build_nbt(
                editor,
                side,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(0 + grid.width // 2, 0, 0),
                    mirror=(False, False, False),
                    diagonal_mirror=True,
                ),
                material_params_func=material_params_func,
            )

        # southwest
        if cell.has_neighbour(south) and cell.has_neighbour(west):
            build_nbt(
                editor,
                inner,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(0, 0, grid.depth - 1),
                    mirror=(False, False, True),
                ),
                material_params_func=material_params_func,
            )
        elif not cell.has_neighbour(south) and not cell.has_neighbour(west):
            build_nbt(
                editor,
                corner,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(0, 0, grid.depth - 1),
                    mirror=(False, False, True),
                ),
                material_params_func=material_params_func,
            )
        elif cell.has_neighbour(south) and not cell.has_neighbour(west):
            build_nbt(
                editor,
                side,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(0, 0, grid.depth // 2),
                    mirror=(False, False, False),
                ),
                material_params_func=material_params_func,
            )
        else:
            build_nbt(
                editor,
                side,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(grid.width // 2, 0, grid.depth - 1),
                    mirror=(True, False, True),
                    diagonal_mirror=True,
                ),
                material_params_func=material_params_func,
            )

        # southeast
        if cell.has_neighbour(south) and cell.has_neighbour(east):
            build_nbt(
                editor,
                inner,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(grid.width - 1, 0, grid.depth - 1),
                    mirror=(True, False, True),
                ),
                material_params_func=material_params_func,
            )
        elif not cell.has_neighbour(south) and not cell.has_neighbour(east):
            build_nbt(
                editor,
                corner,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(grid.width - 1, 0, grid.depth - 1),
                    mirror=(True, False, True),
                ),
                material_params_func=material_params_func,
            )
        elif cell.has_neighbour(south) and not cell.has_neighbour(east):
            build_nbt(
                editor,
                side,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(grid.depth - 1, 0, grid.depth // 2),
                    mirror=(True, False, False),
                ),
                material_params_func=material_params_func,
            )
        else:
            build_nbt(
                editor,
                side,
                cell.plan.palette,
                Transformation(
                    offset=coords + ivec3(grid.width // 2, 0, grid.depth - 1),
                    mirror=(True, False, False),
                    diagonal_mirror=True,
                ),
                material_params_func=material_params_func,
            )

        # northeast
        build_nbt(
            editor,
            corner,
            cell.plan.palette,
            Transformation(
                offset=coords + ivec3(grid.width - 1, 0, 0), mirror=(True, False, False)
            ),
            material_params_func=material_params_func,
        )

        # southwest
        build_nbt(
            editor,
            corner,
            cell.plan.palette,
            Transformation(
                offset=coords + ivec3(0, 0, grid.depth - 1), mirror=(False, False, True)
            ),
            material_params_func=material_params_func,
        )

        # southeast
        build_nbt(
            editor,
            corner,
            cell.plan.palette,
            Transformation(
                offset=coords + ivec3(grid.width - 1, 0, grid.depth - 1),
                mirror=(True, False, True),
            ),
            material_params_func=material_params_func,
        )
