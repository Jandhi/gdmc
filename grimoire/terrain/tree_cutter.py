from gdpc import Editor, Block
from gdpc.vector_tools import ivec3
import time

TREE_LOGS = (
    "minecraft:acacia_log",
    "minecraft:birch_log",
    "minecraft:dark_oak_log",
    "minecraft:jungle_log",
    "minecraft:oak_log",
    "minecraft:spruce_log",
    "minecraft:mangrove_log",
)

MUSHROOM_BLOCKS = (
    "minecraft:mushroom_stem",
    "minecraft:red_mushroom_block",
    "minecraft:brown_mushroom_block",
)

TREE_BLOCKS = (
    TREE_LOGS
    + MUSHROOM_BLOCKS
    + (
        "minecraft:bamboo",
        "minecraft:vine",
        "minecraft:mangrove_roots",
        "minecraft:moss_carpet",
        "minecraft:bee_nest",
    )
)

LEAF_BLOCKS = (
    "minecraft:acacia_leaves",
    "minecraft:birch_leaves",
    "minecraft:dark_oak_leaves",
    "minecraft:jungle_leaves",
    "minecraft:oak_leaves",
    "minecraft:spruce_leaves",
    "minecraft:azalea_leaves",
    "minecraft:mangrove_leaves",
    "minecraft:flowering_azalea_leaves",
)

TREE_AND_LEAF_BLOCKS = TREE_BLOCKS + LEAF_BLOCKS


def log_stems(editor, build_rect, world_slice):
    for x in range(build_rect.size.x):
        for z in range(build_rect.size.y):
            y1 = world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x][z] - 1
            check_pos = ivec3(x, y1, z)
            block_name = world_slice.getBlock(check_pos).id

            if block_name not in TREE_BLOCKS:
                continue
            editor.placeBlock(check_pos, Block("minecraft:air"))
            for y in range(40):
                check_pos = ivec3(x, y1, z) - ivec3(0, y, 0)
                block_name = world_slice.getBlock(check_pos).id

                if block_name in TREE_BLOCKS:
                    # print(block_name)
                    editor.placeBlock(check_pos, Block("minecraft:air"))
                elif block_name == "minecraft:dirt":
                    editor.placeBlock(check_pos, Block("minecraft:grass_block"))
                    continue

                # only continue checking down if its still air and hasn't been caught by the above
                elif block_name != "minecraft:air":
                    continue


def log_trees(editor, build_rect, world_slice):
    for x in range(build_rect.size.x):
        for z in range(build_rect.size.y):
            y1 = world_slice.heightmaps["MOTION_BLOCKING"][x][z] - 1
            check_pos = ivec3(x, y1, z)
            block_name = world_slice.getBlock(check_pos).id

            if block_name not in TREE_AND_LEAF_BLOCKS:
                continue
            editor.placeBlock(check_pos, Block("minecraft:air"))
            for y in range(40):
                check_pos = ivec3(x, y1, z) - ivec3(0, y, 0)
                block_name = world_slice.getBlock(check_pos).id

                if block_name in TREE_AND_LEAF_BLOCKS:
                    # print(block_name)
                    editor.placeBlock(check_pos, Block("minecraft:air"))
                elif block_name == "minecraft:dirt":
                    editor.placeBlock(check_pos, Block("minecraft:grass_block"))
                    continue

                elif block_name != "minecraft:air":
                    continue


# requires player to fly around to allow minecraft to clear all the foliage, and then set gamerule randomtickspeed to something normal. Still much quicker to clear trees
def manual_clear(editor, build_rect, world_slice):
    tile_drops_off = "gamerule doTileDrops false"
    editor.runCommand(tile_drops_off)

    increase_tick_speed = "gamerule randomTickSpeed 4096"
    editor.runCommand(increase_tick_speed)

    log_stems(editor, build_rect, world_slice)
