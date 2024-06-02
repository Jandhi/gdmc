from gdpc import WorldSlice, Editor, Block


def place_relative_to_ground(
    x: int, y: int, z: int, block_name: str, world_slice: WorldSlice, editor: Editor
):
    y_offset = world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x][z] - 1
    editor.placeBlock((x, y + y_offset, z), Block(block_name))


colors = [
    "white",
    "orange",
    "magenta",
    "light_blue",
    "yellow",
    "lime",
    "pink",
    "gray",
    "light_gray",
    "cyan",
    "purple",
    "blue",
    "brown",
    "green",
    "red",
    "black",
]


def get_color(district, districts):
    blocks = colors
    return f"{blocks[districts.calculate_index(district) % len(blocks)]}_wool"


def get_color_differentiated(district, districts, is_water):
    blocks = colors
    suffix = "_terracotta"

    if is_water:
        suffix = "_stained_glass"
    elif district.is_urban:
        suffix = "_wool"

    return blocks[districts.calculate_index(district) % len(blocks)] + suffix
