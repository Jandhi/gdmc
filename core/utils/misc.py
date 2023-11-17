#For generally random helpful functions

from gdpc import Editor, Block, WorldSlice
from gdpc.vector_tools import Rect, ivec2, distance, ivec3
from gdpc.lookup import WATERS

def is_water(point: ivec3, world_slice : WorldSlice):
    block : Block = world_slice.getBlock((point.x, point.y, point.z))
    if block.id in WATERS | {'minecraft:ice', 'minecraft:seagrass'}:
        return True
    return False    