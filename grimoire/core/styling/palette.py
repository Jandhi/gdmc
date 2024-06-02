from enum import Enum, auto

from gdpc import Block

from grimoire.core.assets.asset import Asset
from grimoire.core.styling.blockform import BlockForm
from grimoire.core.styling.colors import MinecraftColor
from grimoire.core.styling.materials.dithering import DitheringPattern
from grimoire.core.styling.materials.material import Material, MaterialParameters


class MaterialRole(Enum):
    PRIMARY_WALL = auto()
    SECONDARY_WALL = auto()

    PRIMARY_ROOF = auto()
    SECONDARY_ROOF = auto()

    PRIMARY_STONE = auto()
    SECONDARY_STONE = auto()

    PRIMARY_WOOD = auto()
    SECONDARY_WOOD = auto()

    PILLAR = auto()


class _ResolutionPriority:
    order: tuple[MaterialRole, ...]
    next_in_line: dict[MaterialRole, MaterialRole]

    def __init__(
        self,
        order: tuple[MaterialRole, ...],
        next_in_line: dict[MaterialRole, MaterialRole],
    ):
        self.order = order
        self.next_in_line = next_in_line

    def get_next_in_line(self, role: MaterialRole) -> MaterialRole | None:
        if role in self.next_in_line:
            return self.next_in_line[role]

        return None


class ResolutionPriority(Enum):
    STONE = _ResolutionPriority(
        order=(
            MaterialRole.PILLAR,
            MaterialRole.PRIMARY_WALL,
            MaterialRole.SECONDARY_WALL,
            MaterialRole.PRIMARY_ROOF,
            MaterialRole.SECONDARY_ROOF,
            MaterialRole.PRIMARY_STONE,
            MaterialRole.SECONDARY_STONE,
            MaterialRole.PRIMARY_WOOD,
            MaterialRole.SECONDARY_WOOD,
        ),
        next_in_line={
            MaterialRole.PRIMARY_WALL: MaterialRole.PRIMARY_STONE,
            MaterialRole.SECONDARY_WALL: MaterialRole.SECONDARY_STONE,
            MaterialRole.PRIMARY_ROOF: MaterialRole.PRIMARY_STONE,
            MaterialRole.SECONDARY_ROOF: MaterialRole.SECONDARY_STONE,
            MaterialRole.PRIMARY_STONE: MaterialRole.PRIMARY_WOOD,
            MaterialRole.SECONDARY_STONE: MaterialRole.SECONDARY_WOOD,
            MaterialRole.PRIMARY_WOOD: MaterialRole.PRIMARY_STONE,
            MaterialRole.SECONDARY_WOOD: MaterialRole.SECONDARY_STONE,
            MaterialRole.PILLAR: MaterialRole.PRIMARY_STONE,
        },
    )

    def order(self) -> tuple[MaterialRole, ...]:
        return self.value.order

    def get_next_in_line(self, role: MaterialRole) -> MaterialRole | None:
        return self.value.get_next_in_line(role)


class Palette(Asset):
    resolution_priority: ResolutionPriority
    materials: dict[MaterialRole, Material]

    # Colors
    primary_color: MinecraftColor
    secondary_color: MinecraftColor

    def find_role(self, block: Block) -> MaterialRole | None:
        role_order = (
            role
            for role in self.resolution_priority.order()
            if role in self.materials and self.materials[role].has_block(block)
        )

        return next(
            role_order,
            None,
        )

    def find_block_id(
        self,
        form: BlockForm,
        parameters: MaterialParameters,
        role: MaterialRole,
    ) -> str | None:
        checked_roles = set()

        while True:
            if role not in self.materials.keys():
                return None

            material = self.materials[role]

            block_id = material.get_id(form, parameters)

            if block_id is not None:
                return block_id

            # Already checked this role before, in cycle
            if role in checked_roles:
                return None
            checked_roles.add(role)

            # Block not found in this role, check next
            role = self.resolution_priority.get_next_in_line(role)

            # End of the line, block not swappable
            if role is None:
                return None


# In short:
#   - Find the role of the block in the input palette
#   - Find the form of the block
#   - Find the id of the block in the new palette of that same role and form
#   - If any of these fail, return the same block
def swap(
    block: Block,
    input_palette: Palette,
    output_palette: Palette,
    parameters: MaterialParameters,
) -> Block:
    role = input_palette.find_role(block)

    if role is None:
        return block

    form = BlockForm.get_form(block)

    new_id = output_palette.find_block_id(form, parameters, role)

    if new_id is None:
        return block

    return Block(id=new_id, states=block.states, data=block.data)
