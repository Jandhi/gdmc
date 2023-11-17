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
from buildings.tests.random_shape import random_shape

SEED = 243

editor = Editor(buffering=True, caching=True)

area = editor.getBuildArea()
editor.transform = (area.begin.x, 0, area.begin.z)

grid = Grid(origin=ivec3(
    x=area.size.x // 2,
    y=-61,
    z=area.size.z // 2,
))
load_assets('assets')

shape = random_shape(SEED)

palette = Palette.find('japanese_dark_blackstone')
plan = BuildingPlan(shape, grid, palette)

build_floor(plan, editor)

build_walls(plan, editor, [
    Wall.find('japanese_wall_bottom_plain'),
    Wall.find('japanese_wall_single_plain'),
    Wall.find('japanese_wall_upper_traps'),
], RNG(SEED, 'build_walls'))
