from typing import TypeVar
from .random import *

T = TypeVar("T")


# Class that wraps the seed value
class Seed:
    def __init__(self, value) -> None:
        self._value = value

    def value(self) -> int:
        return self._value

    # random.py functions
    def randint(self, max: int) -> int:
        return randint(self.value(), max)

    def randrange(self, min: int, max: int) -> int:
        return randrange(self.value(), min, max)

    def choose(self, items: list[T]) -> T:
        return choose(self.value(), items)

    def pop(self, items: list[T]) -> T:
        return pop(self.value(), items)

    def choose_weighted(self, items: dict[T, int]) -> T:
        return choose_weighted(self.value(), items)

    def pop_weighted(self, items: dict[T, int]) -> T:
        return pop_weighted(self.value(), items)

    def odds(self, successes: int, failures: int) -> bool:
        return odds(self.value(), successes, failures)

    def chance(self, successes: int, total: int) -> bool:
        return chance(self.value(), successes, total)

    def percent(self, successes: int) -> bool:
        return self.chance(successes, 100)

    def shuffle(self, items: list) -> list:
        return shuffle(self.value(), items)
