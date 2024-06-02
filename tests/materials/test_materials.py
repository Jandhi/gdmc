# Allows code to be run in root directory
import sys


sys.path[0] = sys.path[0].removesuffix("tests\\materials")

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
class MaterialsTest(EditingTestModule):
    catch_errors = False

    def test(self):
        GlobalSeed.set(173)

        self.init_rng_from_world_seed()
        load_assets(
            "grimoire\\asset_data",
            LoggerSettings(minimum_console_level=LoggingLevel.ERROR),
        )
        self.load_world()

        material: BasicMaterial = Material.find("cobblestone")
        gradient = Gradient(13).with_axis(GradientAxis.x(0, self.build_rect.size.x - 1))

        for x in self.log.progress(range(self.build_rect.size.x), "Building rows"):
            for z in range(self.build_rect.size.y):

                material.place_block(
                    self.editor,
                    BlockForm.BLOCK,
                    {},
                    None,
                    MaterialParameters(
                        position=ivec3(x, 4, z),
                        shade=gradient.calculate_value(
                            ivec3(x, 4, z),
                        ),
                        age=0,
                        moisture=0,
                        dithering_pattern=DitheringPattern.RANDOM_EASE_QUINT,
                    ),
                )
