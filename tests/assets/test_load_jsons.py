# Allows code to be run in root directory
import sys

sys.path[0] = sys.path[0].removesuffix("tests\\assets")

# Actual file
from grimoire.core.structures.nbt.nbt_asset import NBTAsset
from grimoire.core.assets.asset_loader import load_assets


class Test(NBTAsset):
    pass


class SubTest(Test):
    pass


load_assets("tests\\assets")

# you should see one error and two warnings about fields not being annotated
assert len(Test.all()) == 2
assert len(SubTest.all()) == 1
