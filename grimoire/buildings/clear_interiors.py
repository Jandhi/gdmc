from gdpc import Block, Editor
from ..buildings.building_plan import BuildingPlan
from ..core.structures.grid import Grid
from gdpc.vector_tools import ivec3
from ..core.structures.legacy_directions import x_plus, x_minus, z_minus, z_plus


def clear_interiors(plan: BuildingPlan, editor: Editor):
    grid: Grid = plan.grid

    for cell in plan.cells:
        coords = grid.grid_to_local(cell.position) + grid.origin

        x_start = 0 if cell.has_neighbour(x_minus) else 1
        x_end = 0 if cell.has_neighbour(x_plus) else 1

        z_start = 0 if cell.has_neighbour(z_minus) else 1
        z_end = 0 if cell.has_neighbour(z_plus) else 1

        for x in range(x_start, grid.width - x_end):
            for y in range(1, grid.height):
                for z in range(z_start, grid.depth - z_end):
                    editor.placeBlock(coords + ivec3(x, y, z), Block("air"))
