from gdpc.vector_tools import ivec3

from buildings.roofs.roof_data import RoofData
from core.structures.legacy_directions import Direction, vector


# Class to store assets for cells in a building grid
class LegacyCell:
    position: ivec3
    roof_data: RoofData
    plan: any  # will be a building plan
    doors: list[Direction]

    def __init__(self, position: ivec3, plan) -> None:
        self.position = position
        self.plan = plan
        self.doors = []

    def has_neighbour(self, direction: Direction):
        return self.position + vector(direction) in self.plan.cell_map

    def has_door(self, direction: Direction):
        return direction in self.doors

    def get_neighbour(self, direction: Direction):
        pt = self.position + vector(direction)

        if pt not in self.plan.cells:
            return None

        return self.plan.cells[pt]
