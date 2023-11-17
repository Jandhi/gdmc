# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('core\\assets\\tests')

# Actual file
from core.structures.nbt.nbt_asset import NBTAsset
from core.assets.load_assets import load_assets

class Test(NBTAsset):
    pass

class SubTest(Test):
    pass

load_assets('core\\assets\\tests')

# you should see one error and two warnings about fields not being annotated
assert(len(Test.all()) == 2)
assert(len(SubTest.all()) == 1)