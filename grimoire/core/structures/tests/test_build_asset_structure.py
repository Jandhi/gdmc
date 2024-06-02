# Allows code to be run in root directory
import sys

from grimoire.core.maps import get_water_map, get_build_map
from grimoire.landmarks.market.market import Market

sys.path[0] = sys.path[0].removesuffix("\\landmarks\\story")

# Actual file
from gdpc.editor import Editor
from grimoire.core.assets.asset_loader import load_assets
from grimoire.core.structures.asset_structure import AssetStructure
from gdpc.vector_tools import ivec3

SEED = 2

editor = Editor(buffering=True, caching=True)

area = editor.getBuildArea()
print(area)

print("Loading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice loaded!")
water_map = get_water_map(world_slice)
build_map = get_build_map(world_slice, 20)

load_assets("assets")
y = world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][0][0]

test: AssetStructure = AssetStructure.find("well")
"""
build_nbt(
<<<<<<< HEAD
    editor = editor, 
    asset = story,
=======
    editor = editor,
    asset = tests,
>>>>>>> 02c25de9b7a9820350b4fc39db5440fab0975558
    palette = None,
    transformation=Transformation(
        offset= ivec3(area.middle.x,y,area.middle.z),
        mirror=(True, False, True),
        #diagonal_mirror=True,
    ),
)
"""


# well
# test_well = Well(ivec3(area.middle.x,y,area.middle.z))
# test_well.build(editor)

# market
test_market = Market(ivec3(area.middle.x, y, area.middle.z))
test_market.place_block(editor)
