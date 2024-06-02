from gdpc.block import Block
from gdpc.vector_tools import ivec3


# A class derived from an NBT file, assets describing something built in minecraft
# Used to actually construct NBT landmarks
class Structure:
    def __init__(
        self,
        blocks: dict[ivec3 : tuple[int, str]],
        entities: dict[
            ivec3 : tuple[str, str]
        ],  # first str is id of entity, second is nbt
        palette: list[Block],
        dimensions: ivec3,
    ) -> None:
        self.blocks = blocks
        self.entities = entities
        self.palette = palette
        self.width, self.height, self.depth = dimensions
