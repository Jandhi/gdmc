# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\buildings\\tests')

SEED = 1293786

# Actual file
from gdpc.editor import Editor
from core.structures.grid import Grid
from buildings.walls.wall import Wall
#from buildings.roofs.roof import Roof
from buildings.rooms.room import Room


from core.assets.load_assets import load_assets
from core.structures.legacy_directions import cardinal

from palette.palette import Palette
from buildings.roofs import Roof

editor = Editor(buffering=True, caching=True)

from core.noise.rng import RNG

from gdpc.vector_tools import ivec3

area = editor.getBuildArea()
editor.transform = (area.begin.x, 3, area.begin.z)
grid = Grid()
load_assets('assets')

rng = RNG(SEED, 'get_origins')

styles = {
    'japanese' : {
        'lower' : 'japanese_wall_bottom_plain',
        'upper'  : 'japanese_wall_upper_traps',
        'roof'   : 'japanese_roof_flat_brick_single'
    },
    'viking' : {
        'lower'  : 'viking_wall_lower_stone_base_window',
        'upper'  : 'viking_wall_upper_logs_window',
        'roof'   : 'viking_roof_stone_accent_single'
    }
}
style = styles['viking']

# PALETTE
palette : Palette = Palette.find('japanese_dark_blackstone')

# WALLS
lower_wall : Wall = Wall.find(style['lower'])
upper_wall : Wall = Wall.find(style['upper'])

for direction in cardinal:
    grid.build(editor, lower_wall, palette, ivec3(0, 0, 0), direction)
    grid.build(editor, upper_wall, palette, ivec3(0, 1, 0), direction)

# ROOF
roof : Roof = Roof.find(style['roof'])
# roof.build(editor, palette, grid, (0, 2, 0))

# ROOM
room : Room = Room.find('kitchen_no_window_small')
grid.build(editor, room, palette, ivec3(0, 0, 0))