import sys
sys.path[0] = sys.path[0].removesuffix('\\industries\\tests')

from gdpc import Editor
from gdpc.vector_tools import ivec2, ivec3
from data.load_assets import load_assets
from districts.district import District
from terrain.plateau import plateau
from terrain.water_map import get_water_map
from gdpc.world_slice import WorldSlice
from industries import industry, biomes

def detect_biome():
    load_assets('assets')
    editor = Editor(buffering=True, caching=True)

    area = editor.getBuildArea()
    editor.transform = (area.begin.x, 0, area.begin.z)

    print("Loading world slice...")
    build_rect = area.toRect()
    world_slice = editor.loadWorldSlice(build_rect)
    print("World slice loaded!")    # I imagine this is unnecessary, but leaving it in for now

    x0, z0 = 0, 0
    y0 = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][x0][z0]
    district = District(ivec3(x0, z0, y0), True)

    for x in range(build_rect.size.x):
        for z in range(build_rect.size.y):
            if (x, z) == (x0, z0):
                continue

            y = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][x][z]
            district.add_point(ivec3(x, y, z)) 
    # Placeholder until the gruntwork of 'biome -> primary industry -> secondary industry' web is written
    biomes = industry.get_district_biomes(editor, district)
    print(biomes)
    primaries = industry.get_primary_industries(biomes)
    print([primary.name for primary in primaries])

detect_biome()