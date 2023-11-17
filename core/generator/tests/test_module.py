# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\core\\generator\\tests')

from core.generator.module import Module
from core.generator.benchmarking import Benchmark
import time

class TestModule(Module):
    name : str = 'Test'

    @Module.MainClass
    def test(self):
        self.log.debug('test')
        time.sleep(1)

class TestModule2(Module):
    name : str = 'Test2'

    @Module.MainClass
    def test(self):
        for _ in self.log.progress(range(5), 'test2'):
            time.sleep(0.1)

TestModule().test()
TestModule2().test()
TestModule2().test()

Benchmark.print_results()