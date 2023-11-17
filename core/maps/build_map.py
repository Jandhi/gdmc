from gdpc import WorldSlice, Block


def get_build_map(world_slice: WorldSlice):
    size = world_slice.rect.size

    build_map = [[False for _ in range(size.y + 20)] for _ in range(size.x + 20)]  # added a size buffer

    return build_map
