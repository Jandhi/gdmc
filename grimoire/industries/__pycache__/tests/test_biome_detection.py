import sys

sys.path[0] = sys.path[0].removesuffix("\\industries\\tests")

from gdpc import Editor
from gdpc.vector_tools import ivec2, ivec3
from gdpc.world_slice import WorldSlice


def detect_biome():
    editor = Editor(buffering=True, caching=True)

    area = editor.getBuildArea()
    editor.transform = (area.begin.x, 0, area.begin.z)

    print("Loading world slice...")
    build_rect = area.toRect()
    world_slice = editor.loadWorldSlice(build_rect)
    print(
        "World slice loaded!"
    )  # I imagine this is unnecessary, but leaving it in for now

    x = area.size.x // 2
    z = area.size.z // 2
    y = world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x][z]
    player_pos = ivec3(x, y, z)

    print(WorldSlice.getBiome(world_slice, player_pos))
    # Placeholder until the gruntwork of 'biome -> primary industry -> secondary industry' web is written


detect_biome()
