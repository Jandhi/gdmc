from buildings.building_plan import BuildingPlan
from buildings.legacycell import LegacyCell
from core.structures.legacy_directions import cardinal, Direction, up
from gdpc.editor import Editor
from buildings.walls.wall import Wall, LOWER, UPPER
from core.noise.rng import RNG
from core.structures.grid import Grid

NOT_ROOF = 'not_roof'
ONLY_ROOF = 'only_roof'

def build_walls(plan : BuildingPlan, editor : Editor, walls : list[Wall], rng : RNG):
    for cell in plan.cells:
        for direction in cardinal:
            if not cell.has_neighbour(direction):
                build_wall(cell, direction, editor, walls, rng)

def build_wall(cell : LegacyCell, direction : Direction, editor : Editor, walls : list[Wall], rng : RNG):
    has_door = cell.has_door(direction)

    def wall_is_eligible(wall : Wall):
        if wall.has_door != has_door:
            return False
        
        if cell.position.y == 0 and not wall.has_position(LOWER):
            return False
        
        if cell.position.y > 0 and not wall.has_position(UPPER):
            return False
        
        if (not cell.has_neighbour(up)) and NOT_ROOF in wall.tags:
            return False
        
        if cell.has_neighbour(up) and ONLY_ROOF in wall.tags:
            return False
        
        return True


    eligible_walls : list[Wall] = list(filter(wall_is_eligible, walls))

    weighted_walls = {
        wall : wall.weight if wall.weight > 0 else 100 for wall in eligible_walls
    }

    wall : Wall = rng.choose_weighted(weighted_walls)
    grid : Grid = cell.plan.grid

    if wall is None:
        print('Could not find suitable wall, skipped')
        return

    grid.build(editor, wall, cell.plan.palette, cell.position, direction)