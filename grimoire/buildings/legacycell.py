from gdpc.vector_tools import ivec3

from ..buildings.roofs.roof_data import RoofData
from ..core.structures.legacy_directions import LegacyDirection, vector


# Class to store assets for cells in a building grid
class LegacyCell:
    position: ivec3
    roof_data: RoofData
    plan: "BuildingPlan"
    doors: list[LegacyDirection]

    def __init__(self, position: ivec3, plan) -> None:
        self.position = position
        self.plan = plan
        self.doors = []

    def has_neighbour(self, direction: LegacyDirection):
        return self.position + vector(direction) in self.plan.cell_map

    def has_door(self, direction: LegacyDirection):
        return direction in self.doors

    def get_neighbour(self, direction: LegacyDirection):
        pt = self.position + vector(direction)

        return None if pt not in self.plan.cells else self.plan.cells[pt]
