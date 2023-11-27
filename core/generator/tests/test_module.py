# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\core\\generator\\tests')

from core.generator.module import Module
from core.generator.benchmarking import Benchmark
import time

class TestingModule(Module):
    name : str = 'Test'

    @Module.MainClass
    def test(self):
        self.log.debug('tests')
        time.sleep(1)

class TestingModule2(Module):
    name : str = 'Test2'

    @Module.MainClass
    def test(self):
        for _ in self.log.progress(range(5), 'test2'):
            time.sleep(0.1)

TestingModule().test()
TestingModule2().test()
TestingModule2().test()

Benchmark.print_results()