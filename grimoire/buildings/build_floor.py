from gdpc import Block, Editor
from gdpc.vector_tools import ivec3

from ..buildings.building_plan import BuildingPlan
from ..core.structures.grid import Grid
from ..core.styling.blockform import BlockForm
from ..core.styling.materials.material import MaterialParameters
from ..core.styling.palette import MaterialRole


def build_floor(plan: BuildingPlan, editor: Editor, build_ceiling=True):
    """
    Builds the flooring for all cells in a buildingPlan
    """
    grid: Grid = plan.grid

    for cell in plan.cells:

        cell_pos = grid.grid_to_world(cell.position)

        for x in range(grid.width):
            for z in range(grid.depth):
                pos = cell_pos + ivec3(x, 0, z)
                block_id = plan.palette.find_block_id(
                    BlockForm.BLOCK,
                    MaterialParameters(
                        position=pos,
                        age=0,
                        shade=0.5,
                        moisture=0,
                        dithering_pattern=None,
                    ),
                    MaterialRole.SECONDARY_WOOD,
                )
                block = Block(block_id)

                editor.placeBlock(pos, block)

                if build_ceiling:
                    editor.placeBlock(pos + ivec3(0, grid.height - 1, 0), block)
