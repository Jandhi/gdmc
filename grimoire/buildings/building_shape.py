from ..core.assets.asset import Asset, asset_defaults
from gdpc.vector_tools import ivec3, ivec2
from ..core.structures.grid import Grid
from collections.abc import Iterator
from ..core.structures.legacy_directions import (
    z_minus,
    x_z_flip as x_z_flip_dict,
    x_mirror as x_mirror_dict,
    z_mirror as z_mirror_dict,
)


@asset_defaults(door_direction=z_minus)
class BuildingShape(Asset):
    points: list[ivec3]
    door_direction: str

    def on_construct(self) -> None:
        self.points = [ivec3(x, y, z) for (x, y, z) in self.points]

    def get_points(self, grid: Grid) -> Iterator[ivec3]:
        for point in self.points:
            yield from grid.get_points_at(point)

    def get_points_2d(self, grid: Grid) -> Iterator[ivec2]:
        for x, _, z in self.points:
            yield from grid.get_points_at_2d(ivec2(x, z))

    def make_permutations(self):
        for val in range(8):
            x_mirror = (val / 1) % 2 == 0
            z_mirror = (val / 2) % 2 == 0
            x_z_flip = (val / 4) % 2 == 0

            new_points = [ivec3(*point) for point in self.points]
            new_door_direction = self.door_direction

            if x_z_flip:
                for point in new_points:
                    temp = point.x
                    point.x = point.z
                    point.z = temp

                new_door_direction = x_z_flip_dict[new_door_direction]

            if x_mirror:
                for point in new_points:
                    point.x = -point.x

                new_door_direction = x_mirror_dict[new_door_direction]

            if z_mirror:
                for point in new_points:
                    point.z = -point.z

                new_door_direction = z_mirror_dict[new_door_direction]

            if new_points != self.points or self.door_direction != new_door_direction:
                new_shape = BuildingShape()
                new_shape.type = BuildingShape.type_name
                new_shape.points = new_points
                new_shape.door_direction = new_door_direction
                new_shape.name = f"{self.name}_variant_{val}"
                new_shape.add_to_pool()


# Creates variants of shapes
def permute_shapes():
    for shape in BuildingShape.all().copy():
        shape: BuildingShape
        shape.make_permutations()
