from core.assets.asset import Asset, asset_defaults
from gdpc.editor import Editor
from core.structures.grid import Grid
from gdpc.vector_tools import ivec3

# WALL POSITIONS
LOWER = 'lower'
UPPER = 'upper'

# Abstract class for walls
@asset_defaults(has_door=False, weight=1, positions=[LOWER, UPPER])
class Wall(Asset):
    has_door : bool
    weight : int
    positions : list[str]
    
    
    def build(
        self, 
        editor: Editor, 
        grid: Grid, 
        grid_coordinate: ivec3, 
        facing: str = None):
            pass
    
    def has_position(self, pos : str) -> bool:
        return pos in self.positions
       