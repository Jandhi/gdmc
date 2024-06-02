from enum import Enum

from glm import ivec3, ivec2


class Axis:
    def __init__(self, name: str, index: int):
        self.name = name
        self.index = index

    def get(self, vec: ivec3) -> int:
        return vec[self.index]


class Axes:
    X = Axis("x", 0)
    Y = Axis("y", 1)
    Z = Axis("z", 2)
