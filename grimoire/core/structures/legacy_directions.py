from gdpc.vector_tools import ivec2, ivec3

LegacyDirection = str

# By Axis
x_plus = "x_plus"
x_minus = "x_minus"
y_plus = "y_plus"
y_minus = "y_minus"
z_plus = "z_plus"
z_minus = "z_minus"

# By Name
north = z_minus
east = x_plus
south = z_plus
west = x_minus
up = y_plus
down = y_minus
cardinal = (north, east, south, west)

# Compound Directions
northeast = f"{north} and {east}"
northwest = f"{north} and {west}"
southwest = f"{south} and {west}"
southeast = f"{south} and {east}"
all_8 = (north, east, south, west, northeast, northwest, southwest, southeast)

directions = (north, east, south, west, up, down)

opposites = {
    x_plus: x_minus,
    x_minus: x_plus,
    y_plus: y_minus,
    y_minus: y_plus,
    z_plus: z_minus,
    z_minus: z_plus,
}


def opposite(direction):
    return opposites[direction]


vectors = {
    x_plus: ivec3(1, 0, 0),
    x_minus: ivec3(-1, 0, 0),
    y_plus: ivec3(0, 1, 0),
    y_minus: ivec3(0, -1, 0),
    z_plus: ivec3(0, 0, 1),
    z_minus: ivec3(0, 0, -1),
}

for dir1, dir2, compound in (
    (north, east, northeast),
    (north, west, northwest),
    (south, west, southwest),
    (south, east, southeast),
):
    vectors[compound] = vectors[dir1] + vectors[dir2]


def vector(direction: LegacyDirection) -> ivec3:
    return vectors[direction]


def get_ivec2(direction: LegacyDirection) -> ivec2:
    tup = vector(direction)
    return ivec2(tup[0], tup[2])


text_dict = {
    north: "north",
    east: "east",
    south: "south",
    west: "west",
    up: "up",
    down: "down",
}


def to_text(direction):
    return text_dict[direction]


from_text_dict = {
    "north": north,
    "east": east,
    "south": south,
    "west": west,
    "up": up,
    "down": down,
}


def from_text(text: str):
    return from_text_dict[text]


forwards = {north: north, east: east, south: south, west: west}
right = {
    north: east,
    east: south,
    south: west,
    west: north,
}
left = {
    north: west,
    west: south,
    south: east,
    east: north,
}

backwards = opposites

from_ivec2_dict = {
    ivec2(0, -1): north,
    ivec2(0, 1): south,
    ivec2(1, 0): east,
    ivec2(-1, 0): west,
}


def ivec2_to_dir(iv2: ivec2):
    return from_ivec2_dict[iv2]


from_ivec3_dict = {
    ivec3(0, 0, -1): north,
    ivec3(0, 0, 1): south,
    ivec3(1, 0, 0): east,
    ivec3(-1, 0, 0): west,
}


def ivec3_to_dir(iv3: ivec3):
    return from_ivec3_dict[iv3]


x_mirror = {
    x_plus: x_minus,
    x_minus: x_plus,
    z_plus: z_plus,
    z_minus: z_minus,
}

z_mirror = {
    x_plus: x_plus,
    x_minus: x_minus,
    z_plus: z_minus,
    z_minus: z_plus,
}

x_z_flip = {
    x_plus: z_plus,
    x_minus: z_minus,
    z_plus: x_plus,
    z_minus: x_minus,
}
