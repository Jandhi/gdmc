# Allows code to be run in root directory
import sys

sys.path[0] = sys.path[0].removesuffix("\\landmarks\\story")

# Actual file
from gdpc.editor import Editor
from ..core.structures.nbt.build_nbt import build_nbt
from ..core.structures.nbt.nbt_asset import NBTAsset
from ..palette import Palette
from ..core.structures.transformation import Transformation


editor = Editor(transformLike=(0, -60, 0), buffering=True, caching=True)

nbt_asset = NBTAsset.construct(
    name="story",
    type="wall",
    filepath="asset_datawalls/medieval/medieval_stone_wall_door.nbt",
    origin=(0, 0, 0),
    palette=Palette.construct(name="story"),
)

build_nbt(
    editor=editor,
    asset=nbt_asset,
    palette=Palette.construct(name="story"),
    transformation=Transformation(
        mirror=(True, False, False),
        # diagonal_mirror=True,
    ),
)
