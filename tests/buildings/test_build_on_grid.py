# Allows code to be run in root directory
import sys

sys.path[0] = sys.path[0].removesuffix("tests\\buildings")

SEED = 1293786

# Actual file
from gdpc.editor import Editor
from grimoire.core.structures.grid import Grid
from grimoire.buildings.walls.wall import Wall

# from buildings.roofs.roof import Roof
from grimoire.buildings.rooms.room import Room


from grimoire.core.assets.load_assets import load_assets
from grimoire.core.structures.legacy_directions import cardinal

from grimoire.palette import Palette
from grimoire.buildings.roofs.roof import Roof

editor = Editor(buffering=True, caching=True)

from grimoire.core.noise.rng import RNG

from gdpc.vector_tools import ivec3

area = editor.getBuildArea()
editor.transform = (area.begin.x, 3, area.begin.z)
grid = Grid()
load_assets("assets")

rng = RNG(SEED, "get_origins")

styles = {
    "japanese": {
        "lower": "japanese_wall_bottom_plain",
        "upper": "japanese_wall_upper_traps",
        "roof": "japanese_roof_flat_brick_single",
    },
    "viking": {
        "lower": "viking_wall_lower_stone_base_window",
        "upper": "viking_wall_upper_logs_window",
        "roof": "viking_roof_stone_accent_single",
    },
}
style = styles["viking"]

# PALETTE
palette: Palette = Palette.find("japanese_dark_blackstone")

# WALLS
lower_wall: Wall = Wall.find(style["lower"])
upper_wall: Wall = Wall.find(style["upper"])

for direction in cardinal:
    # FIXME: `lower_wall` and `upper_wall` are Wall instead of NBTAsset
    grid.build(editor, lower_wall, palette, ivec3(0, 0, 0), direction)
    grid.build(editor, upper_wall, palette, ivec3(0, 1, 0), direction)

# ROOF
roof: Roof = Roof.find(style["roof"])
# roof.build(editor, palette, grid, (0, 2, 0))

# ROOM
room: Room = Room.find("kitchen_no_window_small")
grid.build(editor, room, palette, ivec3(0, 0, 0))
