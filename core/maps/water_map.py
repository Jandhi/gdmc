from gdpc import WorldSlice, Block
from gdpc.lookup import WATERS


def get_water_map(world_slice: WorldSlice):
    size = world_slice.rect.size

    water_map = [[False for _ in range(size.y)] for _ in range(size.x)]

    for x in range(size.x):
        for z in range(size.y):
            y = world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][x][z]
            block: Block = world_slice.getBlock((x, y - 1, z))

            if block.id in WATERS | {'minecraft:ice', 'minecraft:seagrass'}:
                water_map[x][z] = True

    return water_map
