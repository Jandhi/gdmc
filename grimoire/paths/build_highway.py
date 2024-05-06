import string
from typing import Union

from gdpc import Editor, WorldSlice, Block
from gdpc.vector_tools import ivec3, ivec2

from ..core.noise.random import choose
from ..core.noise.hash import hash
from ..core.structures.legacy_directions import cardinal, get_ivec2, to_text, all_8, ordinal
from ..core.utils.bounds import is_in_bounds2d
from ..core.maps import Map
from ..core.noise.gradient_noise import get_gradient_noise

def build_highway(points : list[ivec3], editor : Editor, world_slice: WorldSlice, map : Map, border = False):
    master_points       : set[ivec2] = set() #Do we need so many sets for this?
    neighbour_points    : set[ivec2] = set()
    border_points       : set[ivec2] = set()
    final_point_heights : dict[ivec2, int] = {} #TODO: Should be merged with below
    border_point_heights: dict[ivec2, int] = {}
    blocks              : dict[ivec2, Block] = {}

    for point in points:
        point_2d = ivec2(point.x, point.z)

        master_points.add(point_2d)
        final_point_heights[point_2d] = point.y

        for direction in cardinal + ordinal:
            neighbour = point_2d + get_ivec2(direction)

            if not is_in_bounds2d(neighbour, world_slice):
                continue

            if neighbour in neighbour_points or neighbour in master_points:
                continue

            neighbour_points.add(neighbour)
            final_point_heights[neighbour] = point.y

    if border:
        #TODO: Extrapolate to function for this and above
        for (point) in neighbour_points:
            for direction in cardinal:
                neighbour = point + get_ivec2(direction)

                if not is_in_bounds2d(neighbour, world_slice):
                    continue

                if neighbour in border_points | master_points | neighbour_points:
                    continue

                border_points.add(neighbour)
                border_point_heights[neighbour] = final_point_heights[point]

    # grab the intended block at each point
    for point in master_points | neighbour_points:
        blocks[point] = get_block(point, final_point_heights, main_path_palette)

    for point in border_point_heights:
        blocks[point] = get_block(point, border_point_heights, border_path_palette)

    place_blocks(final_point_heights, map, world_slice, editor, blocks)
    place_blocks(border_point_heights, map, world_slice, editor, blocks)

def place_blocks(point_heights, map: Map, world_slice: WorldSlice, editor: Editor, blocks: dict[ivec2, Block]):
    for point in point_heights:
        x, z = point
        y = point_heights[point] - 1

        if is_urban_area(point, map):
            continue

        if obstructions_above(point, y, world_slice):
            for i in range(1, 7):
                editor.placeBlock((x, y + i, z), Block('air'))

        editor.placeBlock((x, y, z), blocks[point])

def obstructions_above(point : ivec2, y: int, world_slice : WorldSlice) -> bool:
    return world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][point.x][point.y] > y

def is_urban_area(point: ivec2, map: Map) -> bool:
    return map.districts[point.x][point.y] is not None and map.districts[point.x][point.y].is_urban

def get_block(point : ivec2, point_heights : dict[ivec2, int], palette: dict[float, Union[tuple[Block], Block]]) -> Block:
    y_in_dir = {}
    y = point_heights[point]

    # I think this finds the direction of the path to place stairs and such, but frankly I'm not sure, so I'm leaving it alone
    for direction in cardinal:
        dv = get_ivec2(direction)

        if point + dv not in point_heights:
            continue

        if abs(point_heights[point + dv] - y) >= 2:
            continue

        y_in_dir[direction] = point_heights[point + dv]

        if point - dv not in point_heights:
            continue

        if point_heights[point + dv] == y + 1 and point_heights[point - dv] == y - 1:
            path_dir = to_text(direction)

    return get_from_palette(palette, point)

def get_from_palette(palette : dict[float, Union[tuple[Block], Block]], pos : ivec2, dir: string="None") -> Block:
    value = get_gradient_noise(pos, 4.0)
    block_list = list()
    prev = -1.0
    for key in sorted(palette.keys()):
        if key >= value > prev:
            if palette[key].__class__ == tuple:
                for block in palette[key]:
                    block_list.append(block)
            else:
                block_list.append(palette[key])
        prev = key

    return choose(hash(pos.x * pos.y, pos.x + pos.y), block_list)

# TODO: Replace with palette asset system
main_path_palette = {
    .5: Block("minecraft:packed_mud"),
    1.: Block("minecraft:dirt_path")
}

border_path_palette = {
    .5: Block("minecraft:coarse_dirt"),
    1.: Block("minecraft:rooted_dirt")
}