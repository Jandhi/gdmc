from typing import Optional

from gdpc.editor import Editor
from gdpc.vector_tools import ivec3

from ...core.assets.asset import Asset, asset_defaults
from ...core.structures.grid import Grid

# WALL POSITIONS
LOWER = "lower"
UPPER = "upper"


# Abstract class for walls
@asset_defaults(has_door=False, weight=1, positions=[LOWER, UPPER])
class Wall(Asset):
    has_door: bool
    weight: int
    positions: list[str]

    def build(
        self,
        editor: Editor,
        grid: Grid,
        grid_coordinate: ivec3,
        facing: Optional[str] = None,
    ):
        pass

    def has_position(self, pos: str) -> bool:
        return pos in self.positions
