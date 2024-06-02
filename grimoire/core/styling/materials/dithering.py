from enum import Enum, auto
from typing import Callable

from glm import ivec3

from grimoire.core.noise.seed import Seed
from grimoire.core.utils.easings import ease_in_out


class DitheringPattern(Enum):
    NONE = auto()
    RANDOM = auto()
    RANDOM_EASE_CUBIC = auto()
    RANDOM_EASE_QUINT = auto()
    REGULAR = auto()

    def calculate_index(
        self,
        value: float,
        dimension_range: int,
        position: ivec3,
        seed: Seed,
    ):
        if self == DitheringPattern.NONE:
            step_size = 1.0 / dimension_range
            return int(value / step_size)

        if self == DitheringPattern.REGULAR:
            return calculate_dither_regular(value, dimension_range, position)

        if self == DitheringPattern.RANDOM:
            return calculate_dither_random(value, dimension_range, seed)

        if self == DitheringPattern.RANDOM_EASE_CUBIC:
            return calculate_dither_random(
                value, dimension_range, seed, lambda x: ease_in_out(x, 3)
            )

        if self == DitheringPattern.RANDOM_EASE_QUINT:
            return calculate_dither_random(
                value, dimension_range, seed, lambda x: ease_in_out(x, 5)
            )


def calculate_dither_regular(value: float, range: int, position: ivec3) -> int:
    step_size = 1.0 / (range - 1)  # each step is a range from A to B
    index = int(value / step_size)
    remainder = (value / step_size) - index

    # upper
    if remainder > 3 / 4:
        return index + 1

    # half dither
    if remainder > 1 / 4 and sum(position) % 2 == 0:
        return index + 1

    return index


def calculate_dither_random(
    value: float, range: int, seed: Seed, easing: Callable[[float], float] | None = None
) -> int:
    step_size = 1.0 / (range - 1)  # each step is a range from A to B

    if easing is None:

        def easing(x):
            return x

    index = int(value / step_size)
    remainder = easing((value / step_size) - index)
    percent_chance = int(remainder * 100)

    return index + 1 if seed.percent(percent_chance) else index
