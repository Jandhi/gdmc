from ..core.structures.legacy_directions import Direction
from random import seed
from random import randint
from ..core.structures.market.goods import *

RANDOM = "random"
BASIC = "basic"
TRAPDOOR = "trapdoor"
FENCE_GATE = "fence_gate"
HALF_STAIR = "half_stair"
STAIR = "stair"
HALF_SLAB = "half_slab"
SLAB = "slab"
STAIR_SLAB = "stair_slab"
CAMPFIRE = "campfire"
FENCE = "fence"
BANNER = "banner"
BACK_DOWN = "back_down"
SIDES_DOWN = "sides_down"
FRONT_DOWN = "front_down"
FRONT_BACK_DOWN = "front_back_down"


class Stall:
    # p1 and p2 are the starting and end points of the rectangle that forms the road
    def __init__(
        self,
        origin,
        counter: str = BASIC,
        side: str = BASIC,
        roof: str = BASIC,
        overhang: str = None,
        direction: Direction = "z_minus",
        length: int = 5,
        depth: int = 4,
        height: int = 5,
    ) -> None:
        self.origin = origin
        self.overhang = overhang
        self.counter = counter
        self.roof = roof
        self.side = side
        self.direction = direction
        self.length = length
        self.depth = depth
        self.height = height
        self.back_counter = (
            False  # should there be a duplicate counter at the rear of the stall
        )
        self.counter_space = (
            []
        )  # list of points where there is space to put items on a counter
        self.floor_space = (
            []
        )  # list of points where there is space to put items on a floor
        self.palette: dict = {}

        if self.counter == RANDOM:
            self.randomize_stall()

        if self.side == None or self.side == TRAPDOOR or self.side == FENCE_GATE:
            seed()
            chance_of_back_counter = randint(1, 5)
            if chance_of_back_counter < 5:
                self.back_counter = True

        self.goods = None
        self.set_random_goods()

        self.randomize_colour()

    def get_origin(self):
        return self.origin

    def set_origin(self, origin):
        self.origin = origin

    def set_direction(self, direction):
        self.direction = direction

    def add_counter_space(self, point):
        self.counter_space.append(point)

    def add_floor_space(self, point):
        self.floor_space.append(point)

    def get_floor_good(self):
        seed()
        list_of_goods = self.goods.floor_goods
        a = randint(0, len(list_of_goods) - 1)
        return list_of_goods[a]

    def get_counter_good(self):
        seed()
        list_of_goods = self.goods.counter_goods
        a = randint(0, len(list_of_goods) - 1)
        return list_of_goods[a]

    def has_floor_goods(self):
        if self.goods.floor_goods == False:
            return False
        return True

    def set_random_goods(self):
        seed()
        a = randint(0, 16)  # start at 0 if you want a chance of empty stalls
        if a == 1:
            self.goods = Flower_Shop()
        elif a == 2:
            self.goods = Plant_Shop()
        elif a == 3:
            self.goods = Head_Shop()  # heads don't face correctly atm
        elif a == 4:
            self.goods = Wool_Shop()
        elif a == 5:
            self.goods = Glazed_Terracotta_Shop()
        elif a == 6:
            self.goods = Glass_Shop()
        elif a == 7:
            self.goods = Shulker_Shop()
        elif a == 8:
            self.goods = Fruit_Shop()
        elif a == 9:
            self.goods = Armour_Shop()
        elif a == 10:
            self.goods = Bakery_Shop()
        elif a == 11:
            self.goods = Bell_Pepper_Shop()
        elif a == 12:
            self.goods = Japanese_Shop()
        elif a == 13:
            self.goods = Honey_Shop()
        elif a == 14:
            self.goods = Donut_Shop()
        elif a == 15:
            self.goods = Butcher_Shop()
        elif a == 16:
            self.goods = Alcohol_Shop()

    def randomize_stall(self):
        seed()
        a = randint(1, 6)
        if a == 1:
            self.counter = BASIC
        elif a == 2:
            self.counter = HALF_STAIR
        elif a == 3:
            self.counter = STAIR
        elif a == 4:
            self.counter = HALF_SLAB
        elif a == 5:
            self.counter = STAIR_SLAB
        elif a == 6:
            self.counter = SLAB

        seed()
        a = randint(1, 6)
        if a == 1:
            self.side = BASIC
        elif a == 2:
            self.side = FENCE
        elif a == 3:
            self.side = FENCE_GATE
        elif a == 4:
            self.side = TRAPDOOR
        elif a == 5:
            self.side = STAIR
        elif a == 6:
            self.side = SLAB

        seed()
        a = randint(1, 6)
        if a == 1:
            self.roof = BASIC
        elif a == 2:
            self.roof = BACK_DOWN
        elif a == 3:
            self.roof = SIDES_DOWN
        elif a == 4:
            self.roof = FRONT_DOWN
        elif a == 5:
            self.roof = FRONT_BACK_DOWN

        seed()
        a = randint(1, 4)
        if a == 1:
            self.overhang = None
        elif a == 2:
            self.overhang = TRAPDOOR
        elif a == 3:
            self.overhang = BANNER
        elif a == 4:
            self.overhang = CAMPFIRE

    def randomize_colour(self):
        seed()
        colour_list = (
            "red",
            "white",
            "orange",
            "magenta",
            "light_blue",
            "yellow",
            "lime",
            "pink",
            "gray",
            "light_gray",
            "cyan",
            "blue",
            "purple",
            "brown",
            "green",
            "black",
        )
        a = randint(0, len(colour_list) - 1)
        choice1 = colour_list[a]
        self.palette["market_wool_1"] = f"{choice1}_wool"
        self.palette["market_banner_1"] = f"{choice1}_wall_banner"
        seed()
        a = randint(0, len(colour_list) - 1)
        choice2 = colour_list[a]
        self.palette["market_wool_2"] = f"{choice2}_wool"
        self.palette["market_banner_2"] = f"{choice2}_wall_banner"
