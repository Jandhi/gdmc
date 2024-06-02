from gdpc.editor import Editor
from gdpc.vector_tools import ivec3
from ...core.structures.legacy_directions import north, east, west, south


# uses set block to place blocks with nbts (playerheads)
def place_block(block: str, editor: Editor, point: ivec3, direction=None):
    actual_point = editor.transform.apply(point)
    # setting correct direction
    if direction == west:
        block = block[:11] + "[rotation=12]" + block[11 : len(block)]
    elif direction == east:
        block = block[:11] + "[rotation=4]" + block[11 : len(block)]
    elif direction == south:
        block = block[:11] + "[rotation=8]" + block[11 : len(block)]
    command = f"setblock {actual_point.x} {actual_point.y} {actual_point.z} minecraft:{block} replace"
    editor.runCommand(command)


# summons an entity, mostly used for armor stand
def summon_entity(id: str, nbt: str, editor: Editor, point: ivec3, direction=None):
    actual_point = editor.transform.apply(point)
    # setting correct direction
    if direction == west:
        nbt = nbt[: len(nbt) - 1] + ",Rotation:[90.0f]}"
    elif direction == east:
        nbt = nbt[: len(nbt) - 1] + ",Rotation:[-90.0f]}"
    elif direction == north:
        nbt = nbt[: len(nbt) - 1] + ",Rotation:[180.0f]}"

    summon_entity_command = (
        f"summon {id} {actual_point.x} {actual_point.y} {actual_point.z} {nbt}"
    )
    editor.runCommand(
        summon_entity_command,
        position=ivec3(actual_point.x, actual_point.y, actual_point.z),
    )
