from gdpc.vector_tools import ivec3

from ...assets.asset import Asset, asset_defaults
from grimoire.core.styling.legacy_palette import LegacyPalette
from ...styling.palette import Palette


# Base class with metadata for an NBT file
# We will be subclassing this for different types of landmarks, e.g. walls and rooms
@asset_defaults(
    palette=None,
    do_not_replace=[],
    replace={},
    do_not_place=[],
)
class NBTAsset(Asset):
    # The identifier for the jsons to know what NBTAsset this is
    # By default it is the snake case of the class name.
    # It can be overridden such as here, since n_b_t_asset is silly.
    type_name = "nbtasset"

    filepath: str
    origin: ivec3

    # DEFAULTS
    palette: Palette
    do_not_replace: list[str]  # blocks that should not be swapped by palette swapper
    replace: dict[str, str]  # blocks that must be swapped out
    do_not_place: list[str]  # blocks that shouldn't be placed at all
