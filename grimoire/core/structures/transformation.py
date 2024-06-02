from gdpc.block import Block
from .legacy_directions import (
    x_plus,
    x_minus,
    y_plus,
    y_minus,
    z_plus,
    z_minus,
    from_text,
    to_text,
    directions,
)
from .structure import Structure
from .nbt.nbt_asset import NBTAsset
from gdpc.vector_tools import ivec3

# region Transformation dictionaries
x_mirror = {
    x_plus: x_minus,
    x_minus: x_plus,
    y_plus: y_plus,
    y_minus: y_minus,
    z_plus: z_plus,
    z_minus: z_minus,
}
y_mirror = {
    x_plus: x_plus,
    x_minus: x_minus,
    y_plus: y_minus,
    y_minus: y_plus,
    z_plus: z_plus,
    z_minus: z_minus,
}
z_mirror = {
    x_plus: x_plus,
    x_minus: x_minus,
    y_plus: y_plus,
    y_minus: y_minus,
    z_plus: z_minus,
    z_minus: z_plus,
}
mirror_dicts = (x_mirror, y_mirror, z_mirror)

diagonal_mirror = {
    x_plus: z_plus,
    x_minus: z_minus,
    y_plus: y_plus,
    y_minus: y_minus,
    z_plus: x_plus,
    z_minus: x_minus,
    "x": "z",
    "z": "x",
}
# endregion


# Class to house tranformations of landmarks, including mirroring and offsets
# Rotation is only supported by switching the x/z axis, in other words diagonal_mirror
class Transformation:
    def __init__(
        self,
        offset: ivec3 = None,
        mirror: tuple[bool, bool, bool] = None,
        diagonal_mirror: bool = False,
    ) -> None:
        self.offset = offset or ivec3(0, 0, 0)
        self.mirror = mirror or (False, False, False)
        self.diagonal_mirror = diagonal_mirror

    # Expects text to be in targets
    def apply_to_text(self, text: str) -> str:
        direction = from_text(text)

        # For each dimensinos
        for dim in range(3):
            if self.mirror[dim]:
                direction = mirror_dicts[dim][direction]

        if self.diagonal_mirror:
            direction = diagonal_mirror[direction]

        return to_text(direction)

    def apply_to_palette(self, palette: list[Block]) -> list[Block]:
        return [self.apply_to_block(block) for block in palette]

    def apply_to_block(self, block: Block) -> Block:
        name = block.id
        properties = {}

        for prop_name, prop_value in block.states.items():
            direction_names = [to_text(direction) for direction in directions]

            if prop_name in direction_names:
                properties[self.apply_to_text(prop_name)] = prop_value
            elif prop_value in direction_names:
                properties[prop_name] = self.apply_to_text(prop_value)
            # For axes
            elif prop_value in ("x", "z") and self.diagonal_mirror:
                properties[prop_name] = {"x": "z", "z": "x"}[prop_value]
            # For right and left
            elif prop_value in ("right", "left") and self.mirror[2]:
                properties[prop_name] = {"right": "left", "left": "right"}[prop_value]
            # Everything else
            else:
                properties[prop_name] = prop_value

        return Block(id=name, states=properties)

    def apply_to_point(
        self,
        point: ivec3,
        structure: Structure,
        asset: NBTAsset,
    ) -> ivec3:
        point = ivec3(*point)  # copy point

        # mirroring
        # for now we will not mirror the origin
        if self.mirror[0]:  # x mirror
            point.x = -1 * point.x
        if self.mirror[2]:  # z mirror
            point.z = -1 * point.z

        # rotation(ish)
        if self.diagonal_mirror:
            point = ivec3(point.z, point.y, point.x)

        # Shift according to origin
        origin = self.apply_to_origin(asset.origin)
        point -= origin

        # translation
        point += self.offset

        return point

    def apply_to_origin(self, point: ivec3) -> ivec3:
        origin = ivec3(*point)

        if self.mirror[0]:  # x mirror
            origin = ivec3(-1 * origin.x, origin.y, origin.z)
        if self.mirror[2]:  # z mirror
            origin = ivec3(origin.x, origin.y, -1 * origin.z)

        if self.diagonal_mirror:
            origin = ivec3(origin.z, origin.y, origin.x)

        return origin
