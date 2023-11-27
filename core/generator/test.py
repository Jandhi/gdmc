import abc

from core.generator.module import Module


class TestModule(Module):
    @abc.abstractmethod
    def test(self):
        pass

    @Module.main
    def run(self):
        try:
            self.test()
        except Exception as e:
            self.log.error(f"Test {self.get_name()} failed: {e}")