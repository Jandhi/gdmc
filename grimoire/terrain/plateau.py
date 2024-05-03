from ..districts.district import District
from gdpc import Editor, WorldSlice, Block
from gdpc.vector_tools import ivec2, ivec3
from ..terrain.set_height import set_height

DISTRICT_AVG_RATIO = (
    0.7  # the percent of the height that the districts average should influence
)


def plateau(
    district: District,
    district_map: list[list[District]],
    world_slice: WorldSlice,
    editor: Editor,
    water_map: list[list[bool]],
):
    print(f"Plateauing {district}")

    y_sum = 0.0
    count = 0.0

    for point in district.points:
        y_sum += point.y
        count += 1

    y_avg = y_sum / count
    print(f"{district} has average height {y_avg}")

    for point in district.points:
        if (
            point.x > world_slice.box.size.x or point.z > world_slice.box.size.z
        ):  # bounds check
            continue

        if water_map[point.x][point.z]:  # don't plateau water tiles
            continue

        y = round(DISTRICT_AVG_RATIO * y_avg + (1 - DISTRICT_AVG_RATIO) * point.y)

        set_height(point.x, y, point.z, world_slice, editor)
