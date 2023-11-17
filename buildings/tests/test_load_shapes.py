# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\buildings\\tests')

# Actual file
from buildings.building_shape import BuildingShape
from core.assets.load_assets import load_assets
from gdpc import Editor, Block
from gdpc.vector_tools import ivec3
from core.maps.map import Map
from core.structures.grid import Grid
from core.utils.vectors import point_3d

SEED = 0x6234111
DO_TERRAFORMING = False

load_assets('assets')

shapes = BuildingShape.all()

editor = Editor(buffering=True, caching=True)
load_assets('assets')

area = editor.getBuildArea()
editor.transform = (area.begin.x, 0, area.begin.z)

print("Loading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice loaded!")

map = Map(world_slice)

shape : BuildingShape = BuildingShape.find('quad')

grid = Grid(origin=ivec3(0, 0, 0))

for point in shape.get_points_2d(grid):
    pt_3d = point_3d(point, world_slice)
    pt_3d.y += 10
    editor.placeBlock(pt_3d, Block('glass'))