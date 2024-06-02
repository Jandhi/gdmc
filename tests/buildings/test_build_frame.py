# Allows code to be run in root directory
import sys

from grimoire.buildings.roofs.build_roof import build_roof
from grimoire.buildings.roofs.roof_component import RoofComponent
from grimoire.core.noise.rng import RNG
from grimoire.core.styling.palette import Palette
from tests.buildings.random_shape import random_shape

sys.path[0] = sys.path[0].removesuffix("tests\\buildings")

# Actual file
from gdpc import Editor
from gdpc.vector_tools import ivec3
from grimoire.core.structures.grid import Grid
from grimoire.core.assets.asset_loader import load_assets
from grimoire.buildings.building_plan import BuildingPlan
from grimoire.buildings.walls.build_walls import build_walls
from grimoire.buildings.walls.wall import Wall
from grimoire.core.styling.legacy_palette import LegacyPalette
from grimoire.buildings.build_floor import build_floor

SEED = 0x624AAB

editor = Editor(buffering=True, caching=True)

area = editor.getBuildArea()
editor.transform = (area.begin.x, 0, area.begin.z)

grid = Grid(
    origin=ivec3(
        x=area.size.x // 2,
        y=-61,
        z=area.size.z // 2,
    )
)
load_assets("grimoire/asset_data")

shape = random_shape(SEED)

palette = Palette.find("japanese")
plan = BuildingPlan(shape, grid, palette)
grid.plan = plan

build_floor(plan, editor)

build_walls(
    plan,
    editor,
    [
        Wall.find("japanese_wall_bottom_plain"),
        Wall.find("japanese_wall_single_plain"),
        Wall.find("japanese_wall_upper_traps"),
    ],
    RNG(SEED, "build_walls"),
)

build_roof(
    plan,
    editor,
    [roof for roof in RoofComponent.all() if "japanese" in roof.tags],
    SEED,
)
