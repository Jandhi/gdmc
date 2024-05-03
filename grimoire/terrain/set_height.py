from ..districts.district import District
from gdpc import Editor, WorldSlice, Block
from gdpc.vector_tools import ivec2, ivec3


def set_height(
    x: int, y: int, z: int, world_slice: WorldSlice, editor: Editor, replace_block=None
):
    curr_y = world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x][z]
    block = replace_block or world_slice.getBlock((x, curr_y - 1, z))

    if curr_y > y:
        for py in range(y, curr_y):
            editor.placeBlock((x, py, z), Block("air"))

        editor.placeBlock((x, y - 1, z), block)
    elif curr_y < y:
        for py in range(curr_y, y):
            editor.placeBlock((x, py, z), block)
