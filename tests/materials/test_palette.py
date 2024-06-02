# Allows code to be run in root directory
import sys

from grimoire.core.structures.nbt.nbt_asset import NBTAsset

sys.path[0] = sys.path[0].removesuffix("\\tests\\materials")

# Start of real file

from glm import ivec3

from grimoire.core.styling.blockform import BlockForm
from grimoire.core.generator.test import run_test, EditingTestModule
from grimoire.core.logger import LoggerSettings, LoggingLevel
from grimoire.core.styling.materials.material import DitheringPattern
from grimoire.core.styling.materials.gradient import Gradient, GradientAxis
from grimoire.core.noise.global_seed import GlobalSeed

from grimoire.core.styling.materials.material import (
    Material,
    BasicMaterial,
    MaterialParameters,
)
from grimoire.core.assets.asset_loader import load_assets


@run_test
class PaletteTest(EditingTestModule):
    catch_errors = False

    def test(self):
        GlobalSeed.set(173)

        self.init_rng_from_world_seed()
        load_assets(
            "tests/materials/assets",
            LoggerSettings(minimum_console_level=LoggingLevel.INFO),
        )
        self.load_world()

        asset = NBTAsset.find("test_tower")

        print(asset)
