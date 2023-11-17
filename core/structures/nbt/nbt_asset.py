from core.assets.asset import Asset, asset_defaults
from palette.palette import Palette
from gdpc.vector_tools import ivec3

# Base class with metadata for an NBT file
# We will be subclassing this for different types of structures, e.g. walls and rooms
@asset_defaults(
    palette = None,
    do_not_replace = [], 
    replace = [], 
    do_not_place = [],
)
class NBTAsset(Asset):
    # The identifier for the jsons to know what NBTAsset this is
    # By default it is the snake case of the class name. 
    # It can be overridden such as here, since n_b_t_asset is silly.
    type_name = 'nbtasset' 

    filepath : str
    origin : ivec3
    
    # DEFAULTS
    palette : Palette
    do_not_replace : list[str] # blocks that should not be swapped by palette swapper
    replace : dict[str, str]   # blocks that must be swapped out
    do_not_place : list[str]   # blocks that shouldn't be placed at all

    def on_construct(self) -> None:
        super().on_construct()

        self.origin = ivec3(*self.origin) # convert list to tuple