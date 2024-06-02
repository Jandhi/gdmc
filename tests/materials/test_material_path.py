# Allows code to be run in root directory
import sys

from gdpc.vector_tools import CARDINALS_2D

from grimoire.core.styling.blockform import BlockForm
from grimoire.core.utils.bounds import is_in_bounds2d

sys.path[0] = sys.path[0].removesuffix("tests\\materials")

# Start of real file

from glm import ivec3, ivec2

from grimoire.core.generator.test import run_test, EditingTestModule
from grimoire.core.logger import LoggerSettings, LoggingLevel
from grimoire.core.styling.materials.dithering import DitheringPattern
from grimoire.core.styling.materials.gradient import Gradient, PerlinSettings
from grimoire.core.noise.global_seed import GlobalSeed

from grimoire.core.styling.materials.material import (
    Material,
    BasicMaterial,
    MaterialParameters,
)
from grimoire.core.assets.asset_loader import load_assets


@run_test
class MaterialPathTest(EditingTestModule):
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
        gradient = Gradient(254, perlin_settings=PerlinSettings(23, 6, 1.6, 0.3))

        path = [
            ivec2(i, i)
            for i in range(5, min(self.build_rect.size.x, self.build_rect.size.y) - 5)
        ]

        points = [(point, 0) for point in path]
        visited = set(path)
        max_dist = 10
        queue = points.copy()

        while len(queue) > 0:
            (point, dist) = queue.pop(0)

            if dist == max_dist:
                continue

            for d in CARDINALS_2D:
                neighbour = point + d

                if neighbour in visited:
                    continue

                points.append((neighbour, dist + 1))
                queue.append((neighbour, dist + 1))
                visited.add(neighbour)

        for point, dist in points:
            if not is_in_bounds2d(point, self.world_slice):
                continue

            x, z = point
            y = self.world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x, z] - 1
            pos = ivec3(x, y, z)

            shade_val = gradient.calculate_value(pos, 1 - dist / max_dist)

            if shade_val < 0.5:
                continue

            material.place_block(
                self.editor,
                BlockForm.BLOCK,
                {},
                None,
                MaterialParameters(
                    position=pos,
                    age=0,
                    shade=shade_val,
                    moisture=0,
                    dithering_pattern=DitheringPattern.RANDOM_EASE_CUBIC,
                ),
            )
