from ..districts.district import District
from gdpc import WorldSlice
from gdpc.block import Block
from gdpc.lookup import WATERS, WATER_PLANTS, ICE_BLOCKS
from gdpc.vector_tools import ivec2, ivec3
from .utils.bounds import is_in_bounds
from .utils.bounds import is_in_bounds2d
from .utils.sets.set_operations import find_outline


HIGHWAY = "highway"  # FIXME: Unused variable
CITY_ROAD = "city_road"
BUILDING = "building"
WALL = "Wall"  # FIXME: Unused variable
CITY_WALL = "city_wall"
GATE = "gate"


def get_build_map(world_slice: WorldSlice, buffer: int = 0) -> list[list[bool]]:
    """
    Returns a 2D list representing a build map with dimensions extended by the specified buffer size in the x and z directions.

    Args:
        world_slice: The WorldSlice object containing the size information.
        buffer: An integer specifying the additional size to extend the dimensions by (default is 0).

    Returns:
        A 2D list representing the build map with extended dimensions based on the buffer size.
    """

    size: ivec2 = world_slice.rect.size

    return [[False for _ in range(size.y + buffer)] for _ in range(size.x + buffer)]


def get_building_map(world_slice: WorldSlice):
    size = world_slice.rect.size
    return [[None for _ in range(size.y)] for _ in range(size.x)]


def get_water_map(world_slice: WorldSlice):
    size = world_slice.rect.size

    water_map = [[False for _ in range(size.y)] for _ in range(size.x)]

    for x in range(size.x):
        for z in range(size.y):
            y = world_slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x][z]
            block: Block = world_slice.getBlock((x, y - 1, z))

            if block.id in (WATERS | WATER_PLANTS | ICE_BLOCKS):
                water_map[x][z] = True

    return water_map


# class that carries all the different maps required
class Map:
    water: list[list[bool]]
    districts: list[list[District | None]]
    buildings: list[list[str | None]]
    height: list[list[int]]
    world: WorldSlice
    near_wall: list[list[bool]]  # specifically used for routing roads

    def __init__(self, world_slice: WorldSlice) -> None:
        size = world_slice.rect.size
        self.world = world_slice
        self.districts = self.empty_map()
        self.water = get_water_map(world_slice)
        self.buildings = get_building_map(world_slice)
        self.copy_heightmap()
        self.near_wall = [[False for _ in range(size.y)] for _ in range(size.x)]

    def correct_district_heights(self, districts: list[District]):
        for district in districts:
            for point in district.points:
                point.y = self.world.heightmaps["MOTION_BLOCKING_NO_LEAVES"][point.x][
                    point.z
                ]

    def empty_map(self):
        size = self.world.rect.size
        return [[None for _ in range(size.y)] for _ in range(size.x)]

    def height_at(self, point: ivec2):
        return self.world.heightmaps["MOTION_BLOCKING_NO_LEAVES"][point.x][point.y]

    def copy_heightmap(self):
        size = self.world.rect.size
        self.height = [
            [self.height_at(ivec2(x, y)) for y in range(size.y)] for x in range(size.x)
        ]

    def make_3d(self, point: ivec2):
        return ivec3(point.x, self.height_at(point), point.y)

    def is_in_bounds(self, point: ivec3):
        return is_in_bounds(point, self.world)

    def is_in_bounds2d(self, point: ivec2):
        return is_in_bounds2d(point, self.world)

    def calculate_near_wall(self, districts: list[District]):
        urban_area = set()

        for district in districts:
            urban_area |= district.points_2d

        near_wall_set = find_outline(urban_area, 4) | urban_area

        size = self.world.rect.size
        self.near_wall = [
            [ivec2(x, y) in near_wall_set for y in range(size.y)] for x in range(size.x)
        ]
