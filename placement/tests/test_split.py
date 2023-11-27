# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\placement\\tests')

# Actual file
from gdpc import Editor, Block
from gdpc.vector_tools import ivec2, ivec3
from core.utils.sets.set_operations import split

editor = Editor(buffering=True, caching=True)

area = editor.getBuildArea()
editor.transform = (area.begin.x, 0, area.begin.z)

print("Loading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice loaded!")

points = set()
for x in range(build_rect.size.x):
    for z in range(build_rect.size.y):
        points.add(ivec2(x, z))

a, b = split(points)

for point in a:
    editor.placeBlock(ivec3(point.x, world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][point.x][point.y], point.y), Block('cobblestone'))