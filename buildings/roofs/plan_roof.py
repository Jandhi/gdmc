from buildings.building_plan import BuildingPlan
from core.structures.legacy_directions import cardinal
from buildings.legacycell import LegacyCell
from buildings.roofs.roof_component import CORNER


def plan_roof(plan : BuildingPlan):
    plan.shape.sort(key = lambda point : point[1])

    for pt in plan.shape:
        plan_roof_at_cell(plan, plan.cell_map[pt])

def plan_roof_at_cell(plan : BuildingPlan, cell : LegacyCell):
    up, right, down, left = (cell.has_neighbour(direction) for direction in cardinal)

    # SINGLE
    if not up and not right and not down and not left:
        cell.roof_data.top_left_component     = CORNER
        cell.roof_data.top_right_component    = CORNER
        cell.roof_data.bottom_left_component  = CORNER
        cell.roof_data.bottom_right_component = CORNER