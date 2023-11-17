from time import time
from typing import TypeVar

from colored import Fore, Style

from core.logs.logger import Logger

T = TypeVar("T")


class Benchmark:
    __time_by_name: dict[str, list[float]] = {}

    @staticmethod
    def add_time(name: str, amount: float) -> None:
        if name not in Benchmark.__time_by_name:
            Benchmark.__time_by_name[name] = []

        Benchmark.__time_by_name[name].append(amount)

    @staticmethod
    def log_results(log: Logger) -> None:
        log.display(f'{Fore.dark_gray}----------{Style.reset}')
        log.info('BENCHMARK BY CLASS')

        longest_name = max(len(name) for name in Benchmark.__time_by_name)

        log.info(f'{{:{longest_name}}} {{:>7}} {{:>7}}'.format('Name', 'Average', 'Total'))

        for name, times in Benchmark.__time_by_name.items():
            total = sum(times)
            average = total / len(times)

            log.info(f'{{:{longest_name}}} {{:>7}} {{:>7}}'.format(name, '%.2f' % average, '%.2f' % total))

    @staticmethod
    def print_results() -> None:
        Benchmark.log_results(Logger())

    '''
    Adds a timer to method, logs time elapsed
    '''

    @staticmethod
    def timed(func: T, log: Logger, class_name: str) -> T:
        name = f'{Fore.green}{class_name}{Style.reset}'

        def inner(*args, **kwargs):
            start_time = time()

            log.display(f'{Fore.dark_gray}----------{Style.reset}')
            log.info(f'{name} started')

            func(*args, **kwargs)

            end_time = time()
            time_elapsed = end_time - start_time

            log.info(f'{name} finished after {"%.2f" % time_elapsed} seconds')
            Benchmark.add_time(class_name, time_elapsed)

        return inner
