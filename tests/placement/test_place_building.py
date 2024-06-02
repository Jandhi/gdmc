# Allows code to be run in root directory
import sys

sys.path[0] = sys.path[0].removesuffix("tests\\placement")

# Actual file
from gdpc import Editor, Block
from gdpc.vector_tools import ivec2, ivec3
from grimoire.core.maps import Map
from grimoire.core.assets.asset_loader import load_assets
from grimoire.placement.building_placement import place_building
from grimoire.core.structures.legacy_directions import z_plus
from grimoire.core.noise.rng import RNG


SEED = 0x44444
DO_TERRAFORMING = False

editor = Editor(buffering=True, caching=True)
load_assets("grimoire/asset_data")

area = editor.getBuildArea()
editor.transform = (area.begin.x, 0, area.begin.z)

print("Loading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice loaded!")

map = Map(world_slice)
rng = RNG(SEED)

editor.placeBlock(ivec3(50, 100, 50), Block("glowstone"))
place_building(editor, ivec2(50, 50), map, z_plus, rng, urban_only=False)
