# Allows code to be run in root directory
import sys

from core.generator.test import TestModule
from core.logs.logger import LoggerSettings, LoggingLevel
from core.noise.global_seed import GlobalSeed
from story.names.name_generator import NamingSchema, NameGenerator

sys.path[0] = sys.path[0].removesuffix('story\\names\\tests')

from core.assets.load_assets import load_assets
from story.load_story_types import load_types


class TestNames(TestModule):
    def test(self):
        load_types()
        load_assets("story/names")
        schema: NamingSchema = NamingSchema.all()[0]

        self.log.info(schema.rules)

        GlobalSeed.randomize()
        name_generator = NameGenerator()
        name_generator.set_module_logger_settings(LoggerSettings(
            minimum_console_level=LoggingLevel.ERROR,
            minimum_file_level=LoggingLevel.ERROR,
        ))

        for index in range(10):
            name, args = name_generator.generate_name("name", schema)
            self.log.info(f"Name {index}: {name} with args {args}")


if __name__ == "__main__":
    TestNames().test()
