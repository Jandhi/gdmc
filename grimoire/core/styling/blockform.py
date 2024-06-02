from enum import Enum, auto

from gdpc import Block
from gdpc.lookup import STAIRS, SLABS, WALLS, FENCES, DOORS, TRAPDOORS


class BlockForm(Enum):
    BLOCK = auto()
    STAIRS = auto()
    SLAB = auto()
    WALL = auto()
    FENCE = auto()
    DOOR = auto()
    TRAPDOOR = auto()
    SIGN = auto()

    @staticmethod
    def get_form(block: Block) -> "BlockForm":
        if block.id in STAIRS:
            return BlockForm.STAIRS
        if block.id in SLABS:
            return BlockForm.SLAB
        if block.id in WALLS:
            return BlockForm.WALL
        if block.id in FENCES:
            return BlockForm.FENCE
        if block.id in DOORS:
            return BlockForm.DOOR
        if block.id in TRAPDOORS:
            return BlockForm.TRAPDOOR
        if "sign" in block.id:
            return BlockForm.SIGN

        # We assume otherwise it is a whole block
        # This may not necessarily be the case, but it's a *good enough* metric
        return BlockForm.BLOCK
