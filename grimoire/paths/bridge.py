from gdpc import Editor
from gdpc.vector_tools import line2D
from glm import ivec3

from grimoire.core.generator.module import Module
from grimoire.core.structures.block import Block


class BridgeBuilder(Module):
    @Module.main
    def build_bridge(self, editor: Editor, point_a: ivec3, point_b: ivec3, height: int):
        line = line2D(point_a, point_b)

        for point in line:
            editor.placeBlock(point, Block('cobblestone'))
