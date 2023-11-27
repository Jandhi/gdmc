# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\buildings\\tests')

# Actual file
from gdpc import Editor
from gdpc.vector_tools import ivec3
from core.structures.grid import Grid
from core.assets.load_assets import load_assets
from buildings.building_plan import BuildingPlan
from buildings.walls.build_walls import build_walls
from core.noise.rng import RNG
from buildings.walls.wall import Wall
from palette.palette import Palette
from buildings.build_floor import build_floor
from buildings.roofs.roof_component import RoofComponent
from buildings.roofs.build_roof import build_roof
from buildings.clear_interiors import clear_interiors
from buildings.rooms.furnish import furnish

SEED = 654

editor = Editor(buffering=True, caching=True)

area = editor.getBuildArea()
editor.transform = (area.begin.x, 0, area.begin.z)

grid = Grid(origin=ivec3(
    x = area.size.x // 2,
    y = -61,
    z = area.size.z // 2,
))
load_assets('assets')

shape = [ivec3(0, 0, 0)]

palette = Palette.find('japanese_dark_blackstone')
plan = BuildingPlan(shape, grid, palette)

build_roof(plan, editor, [
    roof for roof in RoofComponent.all() if 'japanese' in roof.tags
], SEED)

clear_interiors(plan, editor)
build_floor(plan, editor)

walls = [
    wall for wall in Wall.all() if 'japanese' in wall.tags
]

build_walls(plan, editor, walls, RNG(SEED, 'build_walls'))

furnish([cell.position for cell in plan.cells], RNG(SEED, 'furnish'), grid, editor, palette)