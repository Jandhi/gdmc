# Allows code to be run in root directory
import sys


sys.path[0] = sys.path[0].removesuffix("\\tests\\terrain")

# Actual file
from gdpc import Editor
from gdpc.vector_tools import ivec2
from grimoire.districts.generate_districts import generate_districts
from grimoire.terrain.smooth import smooth
from grimoire.core.maps import get_water_map
from ..districts.draw_districts import draw_districts

SEED = 36322

editor = Editor(buffering=True, caching=True)

area = editor.getBuildArea()
editor.transform = (area.begin.x, 0, area.begin.z)

print("Loading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice loaded!")

player_pos = ivec2(area.size.x // 2, area.size.z // 2)

water_map = get_water_map(world_slice)
districts, district_map = generate_districts(SEED, build_rect, world_slice, water_map)

for district in districts:
    if not district.is_urban:
        continue

    smooth(district, district_map, world_slice, editor, water_map)


editor.flushBuffer()  # this is needed to reload the world slice properly

print("Reloading worldSlice")
world_slice = editor.loadWorldSlice(build_rect)

draw_districts(districts, build_rect, district_map, water_map, world_slice, editor)
