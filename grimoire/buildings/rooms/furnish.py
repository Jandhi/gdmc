# Actual file
import numpy as np
from gdpc.editor import Editor, Block
from gdpc.vector_tools import ivec3

from ..legacycell import LegacyCell
from ...core.noise.rng import RNG
from ...palette import Palette
from .room import Room
from ...core.structures.grid import Grid
from ...core.structures.legacy_directions import (
    cardinal,
    vector as get_ivec3,
    right,
    up,
    north,
    east,
    south,
    west,
)

ROOM_LIST = [
    "kitchen_no_window_small",
    "kitchen_corner_1",
    "bedroom1",
    "bedroom_centered",
    "bedroom_corner",
    "hallway_1",
    "hallway_aquarium",
    "small_kitchen_with_table",
    "potion_room",
    "storage_room",
    "study",
]

CONNECTION_LIST = ["wall", "open"]

LOWER_STAIRCASE_LIST = ["staircase_corner_lower"]

# NOTE: Unused variable
UPPER_STAIRCASE_LIST = ["staircase_corner_upper"]

ONEBYONE_UPPER_LIST = ["1x1_twostorey_upper_1", "1x1_twostorey_upper_2"]

ONEBYONE_LOWER_LIST = ["1x1_twostorey_lower_1", "1x1_twostorey_lower_2"]

ONEBYONE_LIST = ["1x1_room_1", "1x1_room_2", "1x1_room_3"]


def rotate(a: list, n=1) -> list:
    if not a:
        return a
    n = -n % len(a)  # flip rotation direction
    return np.concatenate((a[n:], a[:n]))


def is_corner(cell_to_check: ivec3, cells_to_fill: list) -> tuple:
    corner_combinations = [
        ["wall", "wall", "open", "open"],
        ["open", "wall", "wall", "open"],
        ["open", "open", "wall", "wall"],
        ["wall", "open", "open", "wall"],
    ]

    test = []
    for direction in cardinal:
        neighbor = cell_to_check + get_ivec3(direction)
        if neighbor in cells_to_fill:
            test.append("open")
        else:
            test.append("wall")

    return test in corner_combinations, test


def build_start(
    cells_with_rooms: list,
    cells_to_fill: list,
    rng: RNG,
    grid: Grid,
    editor: Editor,
    palette: Palette,
    cells: dict[ivec3, LegacyCell],
) -> list:
    start_connections = []
    start = rng.choose(cells_to_fill)
    for direction in cardinal:
        neighbor = start + get_ivec3(direction)
        if neighbor in cells_to_fill or direction in cells[ivec3(*start)].doors:
            start_connections.append("open")
        else:
            start_connections.append("wall")

    # find a room in that fits in that spot
    potential_rooms = []
    for room_name in ROOM_LIST:
        room: Room = Room.find(room_name)
        to_face = room.facing
        for i in range(4):
            if list(rotate(room.connections, i)) == start_connections:
                potential_rooms.append((room, to_face, rotate(room.connections, i)))

            if i > 0:
                to_face = right[to_face]

    room_to_build, room_facing, connections = rng.choose(potential_rooms)
    cells_with_rooms.append((start, connections))

    grid.build(editor, room_to_build, palette, start, facing=room_facing)

    return cells_with_rooms


def build_staircase(
    level: int,
    cells_with_rooms: list,
    cells_to_fill: list,
    rng: RNG,
    grid: Grid,
    editor: Editor,
    palette: Palette,
    cells: dict[ivec3, LegacyCell],
) -> list:
    possible_starts = [
        potential_start
        for potential_start in cells_to_fill
        if (
            is_corner(potential_start, cells_to_fill)[0]
            and potential_start + get_ivec3(up) in cells_to_fill
            and potential_start not in cells_with_rooms
            and list(potential_start)[1] == level
        )
    ]


def build_staircase(
    level: int,
    cells_with_rooms: list,
    cells_to_fill: list,
    rng: RNG,
    grid: Grid,
    editor: Editor,
    palette: Palette,
    cells: dict[ivec3, LegacyCell],
) -> list:
    possible_starts = [
        potential_start
        for potential_start in cells_to_fill
        if (
            is_corner(potential_start, cells_to_fill)[0]
            and potential_start + get_ivec3(up) in cells_to_fill
            and potential_start not in cells_with_rooms
            and list(potential_start)[1] == level
        )
    ]
    start = rng.choose(possible_starts)
    start_connections = is_corner(start, cells_to_fill)[1]

    potential_rooms = []
    for room_name in LOWER_STAIRCASE_LIST:
        room: Room = Room.find(room_name)
        to_face = room.facing
        for i in range(4):
            if list(rotate(room.connections, i)) == start_connections:
                potential_rooms.append((room, to_face, rotate(room.connections, i)))

            if i > 0:
                to_face = right[to_face]

    room_to_build, room_facing, connections = rng.choose(potential_rooms)

    cells_with_rooms.append((start, connections))
    cells_with_rooms.append((start + get_ivec3(up), connections))

    # clear floor for stair
    top_stair_origin = grid.grid_to_world(start + get_ivec3(up))
    for x in range(1, grid.width - 1):
        for z in range(1, grid.depth - 1):
            editor.placeBlock(top_stair_origin + ivec3(x, 0, z), Block("air"))

    grid.build(editor, room_to_build, palette, start, facing=room_facing)
    room_to_build: Room = Room.find("staircase_corner_upper")
    grid.build(
        editor, room_to_build, palette, start + get_ivec3(up), facing=room_facing
    )

    return cells_with_rooms


def get_neighbors(rooms: list, inside_cells: list) -> set:
    neighbors = set()
    for room in rooms:
        for direction in cardinal:
            new_cell = room + get_ivec3(direction)
            if new_cell not in rooms and new_cell in inside_cells:
                neighbors.add(new_cell)
    return neighbors


# FIXME: Refactor
def populate_floor(
    level: int,
    cells_with_rooms: list,
    cells_to_fill: list,
    rng: RNG,
    grid: Grid,
    editor: Editor,
    palette: Palette,
    cells: dict[ivec3, LegacyCell],
) -> list:
    rooms_on_floor = [
        ((x, y, z), con) for (x, y, z), con in cells_with_rooms if y == level
    ]
    cells_on_floor = [(x, y, z) for x, y, z in cells_to_fill if y == level]

    while len(rooms_on_floor) != len(cells_on_floor):
        candidates = []
        # get the connections for the new rooms
        for neighbor in get_neighbors([x for x, y in rooms_on_floor], cells_on_floor):
            north_con, east_con, south_con, west_con = None, None, None, None
            for c, conns in rooms_on_floor:
                for direction in cardinal:
                    if neighbor + get_ivec3(direction) == c:
                        if direction == north:
                            north_con = conns[2]
                        elif direction == east:
                            east_con = conns[3]
                        elif direction == south:
                            south_con = conns[0]
                        elif direction == west:
                            west_con = conns[1]

            for direction in cardinal:
                if (neighbor + get_ivec3(direction)) not in cells_on_floor:
                    if direction == north:
                        north_con = "wall"
                    elif direction == east:
                        east_con = "wall"
                    elif direction == south:
                        south_con = "wall"
                    elif direction == west:
                        west_con = "wall"

            # DOOR CHECK
            if north in cells[ivec3(*neighbor)].doors:
                north_con = "open"
            if south in cells[ivec3(*neighbor)].doors:
                south_con = "open"
            if east in cells[ivec3(*neighbor)].doors:
                east_con = "open"
            if west in cells[ivec3(*neighbor)].doors:
                west_con = "open"

            new_conns = [north_con, east_con, south_con, west_con]

            # i have definitely found the worst way to do this but I just need it to work for now

            potential_rooms = []

            none_idx = [idx for idx, val in enumerate(new_conns) if val is None]
            for i0 in CONNECTION_LIST:
                for i1 in CONNECTION_LIST:
                    for i2 in CONNECTION_LIST:
                        for i3 in CONNECTION_LIST:
                            temp = new_conns
                            for ni in none_idx:
                                if ni == 0:
                                    temp[0] = i0
                                elif ni == 1:
                                    temp[1] = i1
                                elif ni == 2:
                                    temp[2] = i2
                                elif ni == 3:
                                    temp[3] = i3

                            for room_name in ROOM_LIST:
                                room: Room = Room.find(room_name)
                                to_face = room.facing
                                for i in range(4):
                                    if (
                                        list(rotate(room.connections, i)) == temp
                                        and (
                                            room,
                                            to_face,
                                            list(rotate(room.connections, i)),
                                        )
                                        not in potential_rooms
                                    ):
                                        potential_rooms.append(
                                            (
                                                room,
                                                to_face,
                                                tuple(rotate(room.connections, i)),
                                            )
                                        )

                                    if i > 0:
                                        to_face = right[to_face]

            candidates.append((neighbor, len(potential_rooms), potential_rooms))

        min_entropy = min(y for x, y, z in candidates)
        candidates_with_min_entropy = [
            (x, y, z) for x, y, z in candidates if y == min_entropy
        ]

        cell_to_build, _, room_to_build = candidates_with_min_entropy[
            rng.randint(len(candidates_with_min_entropy))
        ]
        room_to_build, room_facing, connections = rng.choose(room_to_build)

        rooms_on_floor.append((cell_to_build, connections))
        cells_with_rooms.append((cell_to_build, connections))
        grid.build(editor, room_to_build, palette, cell_to_build, facing=room_facing)

    return cells_with_rooms


def build_one_by_one(
    num_levels: int,
    cells_to_fill: list,
    rng: RNG,
    grid: Grid,
    editor: Editor,
    palette: Palette,
    cells: dict[ivec3, LegacyCell],
) -> None:
    if num_levels == 1:
        cell = cells_to_fill[0]
        pick = rng.choose(ONEBYONE_LIST)
        room_to_build: Room = Room.find(pick)
        grid.build(editor, room_to_build, palette, cell)
    else:
        cell = [(x, y, z) for x, y, z in cells_to_fill if y == 0][0]
        lower_pick = rng.choose(ONEBYONE_LOWER_LIST)
        upper_pick = rng.choose(ONEBYONE_UPPER_LIST)

        lower_room: Room = Room.find(lower_pick)
        upper_room: Room = Room.find(upper_pick)

        grid.build(editor, lower_room, palette, cell)
        grid.build(editor, upper_room, palette, cell + get_ivec3(up))


def furnish(
    cells_to_fill: list[ivec3],
    rng: RNG,
    grid: Grid,
    editor: Editor,
    palette: Palette,
    cells: dict[ivec3, LegacyCell],
) -> None:
    number_of_floors = max(y for (x, y, z) in cells_to_fill) + 1
    cells_with_rooms = []

    if len(cells_to_fill) == 1 or len(cells_to_fill) == 2 and number_of_floors == 2:
        build_one_by_one(
            number_of_floors, cells_to_fill, rng, grid, editor, palette, cells
        )
    else:
        for level in range(number_of_floors):
            if number_of_floors == 1:
                cells_with_rooms = build_start(
                    cells_with_rooms, cells_to_fill, rng, grid, editor, palette, cells
                )
            elif level != number_of_floors - 1:
                cells_with_rooms = build_staircase(
                    level,
                    cells_with_rooms,
                    cells_to_fill,
                    rng,
                    grid,
                    editor,
                    palette,
                    cells,
                )

            cells_with_rooms = populate_floor(
                level,
                cells_with_rooms,
                cells_to_fill,
                rng,
                grid,
                editor,
                palette,
                cells,
            )
