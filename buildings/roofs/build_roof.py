from gdpc import Editor
from buildings.building_plan import BuildingPlan
from core.structures.grid import Grid
from gdpc.vector_tools import ivec3
from buildings.roofs.roof_component import RoofComponent, CORNER, INNER, SIDE
from core.structures.legacy_directions import north, south, east, west, up
from core.utils.vectors import y_ivec3
from core.structures.nbt.build_nbt import build_nbt
from core.structures.transformation import Transformation
from core.noise.rng import RNG

def build_roof(plan : BuildingPlan, editor : Editor, roofComponents : list[RoofComponent], seed : int):
    grid : Grid = plan.grid
    rng = RNG(seed, 'build_roof')
    
    def roof_is_shape(shape : str):
        return lambda roof : roof.shape == shape
    
    corners = list(filter(roof_is_shape(CORNER), roofComponents))
    inners  = list(filter(roof_is_shape(INNER ), roofComponents))
    sides   = list(filter(roof_is_shape(SIDE  ), roofComponents))

    corner = rng.choose(corners)
    inner  = rng.choose(inners)
    side   = rng.choose(sides)

    # northwest
    for cell in plan.cells:
        if cell.has_neighbour(up):
            continue

        coords = grid.grid_to_local(cell.position + y_ivec3(1)) + grid.origin
        transform_vecs = {
            north : ivec3(0, 0, 0), # northwest
            east: ivec3(grid.width - 1, 0, 0), # northeast
            south: ivec3(0, 0, grid.depth - 1), # southeast
            west: ivec3(grid.width - 1, 0, grid.depth - 1), # southwest
        }

        # northwest
        if cell.has_neighbour(north) and cell.has_neighbour(west):
            build_nbt(editor, inner, cell.plan.palette, Transformation(
                offset = coords + ivec3(0, 0, 0),
            ))
        elif not cell.has_neighbour(north) and not cell.has_neighbour(west):
            build_nbt(editor, corner, cell.plan.palette, Transformation(
                offset = coords + ivec3(0, 0, 0),
            ))
        elif cell.has_neighbour(north) and not cell.has_neighbour(west):
            build_nbt(editor, side, cell.plan.palette, Transformation(
                offset = coords + ivec3(0, 0, grid.depth // 2),
                mirror=(False, False, True),
            ))
        else:
            build_nbt(editor, side, cell.plan.palette, Transformation(
                offset = coords + ivec3(grid.width // 2, 0, 0),
                mirror=(False, False, True),
                diagonal_mirror=True,
            ))

        # northeast
        if cell.has_neighbour(north) and cell.has_neighbour(east):
            build_nbt(editor, inner, cell.plan.palette, Transformation(
                offset = coords + ivec3(grid.width - 1, 0, 0),
                mirror=(True, False, False),
            ))
        elif not cell.has_neighbour(north) and not cell.has_neighbour(east):
            build_nbt(editor, corner, cell.plan.palette, Transformation(
                offset = coords + ivec3(grid.width - 1, 0, 0),
                mirror=(True, False, False),
            ))
        elif cell.has_neighbour(north) and not cell.has_neighbour(east):
            build_nbt(editor, side, cell.plan.palette, Transformation(
                offset = coords + ivec3(grid.width - 1, 0, grid.depth // 2),
                mirror=(True, False, True),
            ))
        else:
            build_nbt(editor, side, cell.plan.palette, Transformation(
                offset = coords + ivec3(0 + grid.width // 2, 0, 0),
                mirror=(False, False, False),
                diagonal_mirror=True,
            ))

        

        # southwest
        if cell.has_neighbour(south) and cell.has_neighbour(west):
            build_nbt(editor, inner, cell.plan.palette, Transformation(
                offset = coords + ivec3(0, 0, grid.depth - 1),
                mirror=(False, False, True),
            ))
        elif not cell.has_neighbour(south) and not cell.has_neighbour(west):
            build_nbt(editor, corner, cell.plan.palette, Transformation(
                offset = coords + ivec3(0, 0, grid.depth - 1),
                mirror=(False, False, True),
            ))
        elif cell.has_neighbour(south) and not cell.has_neighbour(west):
            build_nbt(editor, side, cell.plan.palette, Transformation(
                offset = coords + ivec3(0, 0, grid.depth // 2),
                mirror=(False, False, False),
            ))
        else:
            build_nbt(editor, side, cell.plan.palette, Transformation(
                offset = coords + ivec3(grid.width // 2, 0, grid.depth - 1),
                mirror=(True, False, True),
                diagonal_mirror=True,
            ))

        # southeast
        if cell.has_neighbour(south) and cell.has_neighbour(east):
            build_nbt(editor, inner, cell.plan.palette, Transformation(
                offset = coords + ivec3(grid.width - 1, 0, grid.depth - 1),
                mirror=(True, False, True),
            ))
        elif not cell.has_neighbour(south) and not cell.has_neighbour(east):
            build_nbt(editor, corner, cell.plan.palette, Transformation(
                offset = coords + ivec3(grid.width - 1, 0, grid.depth - 1),
                mirror=(True, False, True),
            ))
        elif cell.has_neighbour(south) and not cell.has_neighbour(east):
            build_nbt(editor, side, cell.plan.palette, Transformation(
                offset = coords + ivec3(grid.depth - 1, 0, grid.depth // 2),
                mirror=(True, False, False),
            ))
        else:
            build_nbt(editor, side, cell.plan.palette, Transformation(
                offset = coords + ivec3(grid.width // 2, 0, grid.depth - 1),
                mirror=(True, False, False),
                diagonal_mirror=True,
            ))

        continue

        # northeast
        build_nbt(editor, corner, cell.plan.palette, Transformation(
            offset=coords + ivec3(grid.width - 1, 0, 0),
            mirror=(True, False, False)
        ))

        # southwest
        build_nbt(editor, corner, cell.plan.palette, Transformation(
            offset=coords + ivec3(0, 0, grid.depth - 1),
            mirror=(False, False, True)
        ))
        
        # southeast
        build_nbt(editor, corner, cell.plan.palette, Transformation(
            offset=coords + ivec3(grid.width - 1, 0, grid.depth - 1),
            mirror=(True, False, True)
        ))