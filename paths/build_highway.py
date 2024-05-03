import string
from typing import Union

from gdpc import Editor, WorldSlice, Block
from gdpc.vector_tools import ivec3, ivec2

from core.noise.random import choose
from core.noise.hash import hash
from core.structures.legacy_directions import cardinal, get_ivec2, to_text
from core.utils.bounds import is_in_bounds2d
from core.maps.map import Map
from core.noise.gradient_noise import get_gradient_noise

def build_highway(points : list[ivec3], editor : Editor, world_slice: WorldSlice, map : Map, path_width: int = 1, border = False):
    master_points       : set[ivec2] = set()
    neighbour_points    : set[ivec2] = set()
    border_points       : set[ivec2] = set()
    final_point_heights : dict[ivec2, int] = {}
    border_point_heights: dict[ivec2, int] = {}
    blocks              : dict[ivec2, Block] = {}

    # loops all points in the highway
    for point in points:
        point_2d = ivec2(point.x, point.z)

        master_points.add(point_2d)
        final_point_heights[point_2d] = point.y

        # adds the neighbours to a set
        for x in range(-1*path_width, path_width+1):
            for z in range(-1*path_width, path_width+1):
                neighbour = point_2d + ivec2(x, z)

                if not is_in_bounds2d(neighbour, world_slice):
                    continue

                if neighbour in neighbour_points or neighbour in master_points:
                    continue

                neighbour_points.add(neighbour)
                final_point_heights[neighbour] = point.y # this is an estimate of height to help the next step

    if border:
        for (point) in neighbour_points:
            for dir in cardinal:
                neighbour = point + get_ivec2(dir)

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

    # place the blocks
    for point in final_point_heights:
        x, z = point
        y = final_point_heights[point] - 1

        # don't place in urban area
        if map.districts[x][z] is not None and map.districts[x][z].is_urban:
            continue

        if world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][x][z] > y:
            for i in range(1, 7):
                editor.placeBlock((x, y + i, z), Block('air'))

        editor.placeBlock((x, y, z), blocks[point])

    for point in border_point_heights:
        x, z = point
        y = border_point_heights[point] - 1

        if world_slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][x][z] > y:
            for i in range(1, 7):
                editor.placeBlock((x, y + i, z), Block('air'))

        editor.placeBlock((x, y, z), blocks[point])


def get_block(point : ivec2, point_heights : dict[ivec2, int], palette: dict[float, Union[tuple[Block], Block]]) -> Block:
    y_in_dir = {}
    y = point_heights[point]

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
        
    # if all(y_in_dir[direction] < y for direction in y_in_dir) and point_heights[point] > 0:
    #     point_heights[point] -= 1
    #     return get_block(point, point_heights, palette)

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

# Note the value distribution is NOT uniform, but the mean is .5, and they are relatively normally distributed
main_path_palette = {
    .5: Block("minecraft:packed_mud"),
    1.: Block("minecraft:dirt_path")
}

border_path_palette = {
    .5: Block("minecraft:coarse_dirt"),
    1.: Block("minecraft:rooted_dirt")
}