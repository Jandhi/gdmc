# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\terrain\\tests')

# Actual file
from gdpc import Editor
from gdpc.vector_tools import ivec3
from districts.district import District
from terrain.plateau import plateau
from core.maps.water_map import get_water_map

SEED = 36322

editor = Editor(buffering=True, caching=True)

area = editor.getBuildArea()
editor.transform = (area.begin.x, 0, area.begin.z)

print("Loading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice loaded!")

x0, z0 = 0, 0
y0 = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][x0][z0]
district = District(ivec3(x0, z0, y0), True)
water_map = get_water_map(world_slice)

district_map = [[district for _ in range(build_rect.size.y)] for _ in range(build_rect.size.x)]

for x in range(build_rect.size.x):
    for z in range(build_rect.size.y):
        if (x, z) == (x0, z0):
            continue

        y = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][x][z]
        district.add_point(ivec3(x, y, z))

plateau(district, district_map, world_slice, editor, water_map)