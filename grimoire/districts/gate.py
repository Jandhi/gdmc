from gdpc import Editor, Block
from gdpc.vector_tools import ivec2, ivec3
from gdpc import WorldSlice
from ..core.structures.legacy_directions import north, east, south, vector, ivec3_to_dir
from ..core.utils.geometry import is_straight_not_diagonal_ivec2
from ..core.structures.nbt.build_nbt import build_nbt
from ..core.structures.nbt.nbt_asset import NBTAsset
from ..core.structures.transformation import Transformation
from ..palette import Palette


# Class to track gate assets
class Gate:
    location: ivec3
    direction: str

    def __init__(self, location: ivec3, direction: str) -> None:
        self.location = location
        self.direction = direction


def add_gates(
    wall_list: list,
    editor: Editor,
    world_slice: WorldSlice,
    is_thin: bool,
    inner_wall_dict: dict,
    palette: Palette,
    palisade: bool = False,
) -> list[Gate]:
    distance_to_next_gate = 30  # minimum
    gate_possible = 0  # counter if 0, allow a tower to be built
    height_map = world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]

    gates: list[Gate] = []

    basic_wide_gate = NBTAsset.construct(
        name="gate",
        type="gate",
        filepath="grimoire/asset_data/city_wall/gates/basic_wide_gate.nbt",
        origin=(3, 1, 3),
        palette=Palette.find("wall_palette"),
    )

    basic_thin_gate = NBTAsset.construct(
        name="gate",
        type="gate",
        filepath="grimoire/asset_data/city_wall/gates/basic_thin_gate.nbt",
        origin=(1, 1, 3),
        palette=Palette.find("wall_palette"),
    )

    basic_palisade_gate = NBTAsset.construct(
        name="gate",
        type="gate",
        filepath="grimoire/asset_data/city_wall/gates/basic_palisade_gate.nbt",
        origin=(1, 1, 2),
        palette=Palette.find("wall_palette"),
    )

    for i, wall_point in enumerate(wall_list):
        if palisade:
            point = ivec3(wall_point[0], wall_point[1], wall_point[2])
            if gate_possible == 0:
                # TODO if conditions like this should be separated out into a variable beforehand
                if (
                    i < len(wall_list) - 7
                    and is_straight_not_diagonal_ivec2(
                        ivec2(point.x, point.z),
                        ivec2(wall_list[i + 6][0], wall_list[i + 6][2]),
                        6,
                    )
                    and abs(point.y - wall_list[i + 6][1]) <= 1
                ):
                    middle_point = ivec3(
                        wall_list[i + 2][0], wall_list[i + 2][1], wall_list[i + 2][2]
                    )
                    if point.x == wall_list[i + 6][0]:
                        dir = east
                    else:
                        dir = north
                    if dir in (north, south):
                        neighbours = [
                            ivec2(x, z)
                            for x in range(middle_point.x - 2, middle_point.x + 3)
                            for z in range(middle_point.z - 1, middle_point.z + 2)
                        ]
                    else:
                        neighbours = [
                            ivec2(x, z)
                            for x in range(middle_point.x - 1, middle_point.x + 2)
                            for z in range(middle_point.z - 2, middle_point.z + 3)
                        ]
                    height = height_map[middle_point.x, middle_point.z]
                    gate_possible = distance_to_next_gate
                    for height in range(height, height + 10):
                        for neighbour in neighbours:
                            editor.placeBlock(
                                (neighbour.x, height, neighbour.y),
                                Block("minecraft:air"),
                            )
                    # build gate
                    diagonal_mirror = False
                    if dir in (north, south):
                        diagonal_mirror = True

                    location = ivec3(
                        middle_point.x,
                        height_map[middle_point.x, middle_point.z],
                        middle_point.z,
                    )
                    gates.append(Gate(location, dir))

                    build_nbt(
                        editor=editor,
                        asset=basic_palisade_gate,
                        transformation=Transformation(
                            offset=location,
                            mirror=(True, False, False),
                            diagonal_mirror=diagonal_mirror,
                        ),
                        palette=palette,
                    )
            else:
                gate_possible -= 1
        else:
            point = wall_point[0]
            if gate_possible == 0:
                if (
                    i < len(wall_list) - 7
                    and is_straight_not_diagonal_ivec2(
                        ivec2(point.x, point.z),
                        ivec2(wall_list[i + 6][0].x, wall_list[i + 6][0].z),
                        6,
                    )
                    and abs(point.y - wall_list[i + 6][0].y) <= 1
                ):
                    if is_thin:
                        middle_point = wall_list[i + 3][0]
                        dir = vector(wall_list[i + 3][1][0])
                        if ivec3_to_dir(dir) in (north, south):
                            neighbours = [
                                ivec2(x, z)
                                for x in range(middle_point.x - 3, middle_point.x + 4)
                                for z in range(middle_point.z - 1, middle_point.z + 2)
                            ]
                        else:
                            neighbours = [
                                ivec2(x, z)
                                for x in range(middle_point.x - 1, middle_point.x + 2)
                                for z in range(middle_point.z - 3, middle_point.z + 4)
                            ]
                        height = height_map[middle_point.x, middle_point.z]
                        gate_possible = distance_to_next_gate
                        for height in range(height, height + 6):
                            for neighbour in neighbours:
                                editor.placeBlock(
                                    (neighbour.x, height, neighbour.y),
                                    Block("minecraft:air"),
                                )
                        # build gate
                        diagonal_mirror = False
                        if ivec3_to_dir(dir) in (north, south):
                            diagonal_mirror = True

                        location = ivec3(
                            middle_point.x,
                            height_map[middle_point.x, middle_point.z],
                            middle_point.z,
                        )
                        gates.append(Gate(location, ivec3_to_dir(dir)))

                        build_nbt(
                            editor=editor,
                            asset=basic_thin_gate,
                            transformation=Transformation(
                                offset=location,
                                mirror=(True, False, False),
                                diagonal_mirror=diagonal_mirror,
                            ),
                            palette=palette,
                        )
                    else:
                        dir = vector(wall_list[i + 3][1][0])
                        middle_point = wall_list[i + 3][0] + dir * 2
                        # checking inner wall, if it is not where it is expected to be, not a valid gate location

                        for a in range(i, i + 7):
                            inner_wall_pt = wall_list[a][0] + dir * 4
                            if (
                                inner_wall_dict.get(
                                    ivec2(inner_wall_pt.x, inner_wall_pt.z)
                                )
                                == None
                            ):
                                break
                            # prep gate
                            if a == i + 6:
                                neighbours = [
                                    ivec2(x, z)
                                    for x in range(
                                        middle_point.x - 3, middle_point.x + 4
                                    )
                                    for z in range(
                                        middle_point.z - 3, middle_point.z + 4
                                    )
                                ]
                                height = height_map[middle_point.x, middle_point.z]
                                gate_possible = distance_to_next_gate
                                for height in range(height, height + 6):
                                    for neighbour in neighbours:
                                        editor.placeBlock(
                                            (neighbour.x, height, neighbour.y),
                                            Block("minecraft:air"),
                                        )

                                # build gate
                                diagonal_mirror = False
                                if ivec3_to_dir(dir) in (north, south):
                                    diagonal_mirror = True

                                location = ivec3(
                                    middle_point.x,
                                    height_map[middle_point.x, middle_point.z],
                                    middle_point.z,
                                )
                                gates.append(Gate(location, ivec3_to_dir(dir)))

                                build_nbt(
                                    editor=editor,
                                    asset=basic_wide_gate,
                                    transformation=Transformation(
                                        offset=location,
                                        mirror=(True, False, False),
                                        diagonal_mirror=diagonal_mirror,
                                    ),
                                    palette=palette,
                                )
            else:
                gate_possible -= 1

    return gates
