from gdpc import WorldSlice

HIGHWAY = 'highway'
CITY_ROAD = 'city_road'
BUILDING = 'building'
WALL = 'Wall'
CITY_WALL = 'city_wall'
GATE = 'gate'

def get_building_map(world_slice : WorldSlice):
    size = world_slice.rect.size
    return [[None for _ in range(size.y)] for _ in range(size.x)]