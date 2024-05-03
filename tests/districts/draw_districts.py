from gdpc.vector_tools import ivec3

from .place_colors import get_color_differentiated, place_relative_to_ground


def draw_districts(districts, build_rect, district_map, water_map, world_slice, editor):
    print("Drawing districts")
    for x in range(build_rect.size.x):
        for z in range(build_rect.size.y):
            district = district_map[x][z]

            if district is None:
                continue

            block = get_color_differentiated(district, districts, water_map[x][z])
            place_relative_to_ground(x, 0, z, block, world_slice, editor)

            y = world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x][z]
            if ivec3(x, y, z) in district.edges:
                place_relative_to_ground(x, -1, z, block, world_slice, editor)
                place_relative_to_ground(x, 0, z, "glass", world_slice, editor)
