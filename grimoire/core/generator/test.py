import abc
from abc import ABC

from gdpc import Editor, Rect, WorldSlice

from ...core.generator.module import Module


def run_test(cls):
    mod: TestModule = cls()
    mod.run()
    return cls


class TestModule(Module):
    catch_errors: bool = True

    @abc.abstractmethod
    def test(self):
        pass

    @Module.main
    def run(self):
        if self.catch_errors:
            try:
                self.test()
            except Exception as e:
                self.log.error(f"Test {self.get_name()} failed: {e}")
        else:
            self.test()


class EditingTestModule(TestModule, ABC):
    editor: Editor
    build_rect: Rect
    world_slice: WorldSlice

    def load_world(self):
        self.editor = Editor(buffering=True, caching=True)
        area = self.editor.getBuildArea()
        self.editor.transform = (area.begin.x, 0, area.begin.z)

        self.log.info("Loading world slice...")

        self.build_rect = area.toRect()
        self.world_slice = self.editor.loadWorldSlice(self.build_rect)

        self.log.info("World slice loaded!")
