from gdpc import WorldSlice
from gdpc.vector_tools import ivec3, ivec2
from typing import Iterator, TypeVar

T = TypeVar("T")


def clamp(value: T, minimum: T, maximum: T) -> T:
    return min(maximum, max(minimum, value))


def is_in_bounds(point: ivec3, world_slice: WorldSlice) -> bool:
    return (
        point.x >= 0
        and point.z >= 0
        and point.x < world_slice.box.size.x
        and point.z < world_slice.box.size.z
    )


def is_in_bounds2d(point: ivec2, world_slice: WorldSlice) -> bool:
    return (
        point.x >= 0
        and point.y >= 0
        and point.x < world_slice.box.size.x
        and point.y < world_slice.box.size.z
    )


def area_2d(size: ivec2) -> Iterator[ivec2]:
    for x in range(size.x):
        for y in range(size.y):
            yield ivec2(x, y)
