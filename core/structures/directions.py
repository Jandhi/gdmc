class Direction2D:
    x : int
    z : int

    def __init__(self, x : int, z : int) -> None:
        self.x = x
        self.z = z

    # Array access
    def __getitem__(self, index : int) -> int:
        return [self.x, self.z][index]
    
    def __setitem__(self, index : int, value : int) -> None:
        if index == 0:
            self.x = value
        elif index == 1:
            self.z = value

    # Unary
    def __neg__(self) -> 'Direction2D':
        return Direction2D(-self.x, -self.z)
    
    def __pos__(self) -> 'Direction2D':
        return Direction2D(self.x, self.z)
    
    def __abs__(self) -> 'Direction2D':
        return Direction2D(*map(abs, self))
    
    # Equality
    def __eq__(self, other : any) -> bool:
        return self.x == other[0] and \
               self.z == other[1]
    def __ne__(self, other : any) -> bool:
        return self.x != other[0] or \
               self.z != other[1]

    # Adding
    def __add__(self, other) -> 'Direction2D':
        return Direction2D(self.x + other[0], self.z + other[1])
    
    def __radd__(self, other) -> 'Direction2D':
        return Direction2D(self.x + other[0], self.z + other[1])
    
    def __iadd__(self, other) -> 'Direction2D':
        self.x += other[0]
        self.z += other[1]

    # Subtracting
    def __sub__(self, other) -> 'Direction2D':
        return Direction2D(self.x - other[0], self.z - other[1])
    
    def __rsub__(self, other) -> 'Direction2D':
        return Direction2D(other[0] - self.x, other[1] - self.z)
    
    def __isub__(self, other) -> 'Direction2D':
        self.x -= other[0]
        self.z -= other[1]

    # Multiplication
    def __mul__(self, value : int) -> 'Direction2D':
        return Direction2D(self.x * value, self.z * value)
    
    def __rmul__(self, value : int) -> 'Direction2D':
        return Direction2D(value * self.x, value * self.z)
    
    # Turns
    def opposite(self) -> 'Direction2D':
        return -self
    
    def right(self) -> 'Direction2D':
        return Direction2D(-self.z, self.x)
    
    def left(self) -> 'Direction2D':
        return Direction2D(self.z, -self.x)
    
    # Utility
    def __hash__(self):
        return hash(tuple(self))
    
    def to_3D(self) -> 'Direction':
        return Direction(self.x, 0, self.z)
    
    # Display
    def __repr__(self) -> str:
        return f'Dir2D({self.x}, {self.z})'

    def text(self) -> str:
        if self.to_3D() == Directions.North:
            return 'north'
        if self.to_3D() == Directions.South:
            return 'south'
        if self.to_3D() == Directions.East:
            return 'east'
        if self.to_3D() == Directions.West:
            return 'west'
        
        raise ValueError(f'Direction {self} can\'t be converted to text')

class Direction:
    x : int
    y : int
    z : int

    def __init__(self, x : int, y : int, z : int) -> None:
        self.x = x
        self.y = y
        self.z = z

    # Array access
    def __getitem__(self, index : int) -> int:
        return [self.x, self.y, self.z][index]
    
    def __setitem__(self, index : int, value : int) -> None:
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value

    # Unary
    def __neg__(self) -> 'Direction':
        return Direction(-self.x, -self.y, -self.z)
    
    def __pos__(self) -> 'Direction':
        return Direction(self.x, self.y, self.z)
    
    def __abs__(self) -> 'Direction':
        return Direction(*map(abs, self))
    
    # Equality
    def __eq__(self, other : any) -> bool:
        return self.x == other[0] and \
               self.y == other[1] and \
               self.z == other[2]
    def __ne__(self, other : any) -> bool:
        return self.x != other[0] or \
               self.y != other[1] or \
               self.z != other[2]

    # Adding
    def __add__(self, other) -> 'Direction':
        return Direction(self.x + other[0], self.y + other[1], self.z + other[2])
    
    def __radd__(self, other) -> 'Direction':
        return Direction(self.x + other[0], self.y + other[1], self.z + other[2])
    
    def __iadd__(self, other) -> 'Direction':
        self.x += other[0]
        self.y += other[1]
        self.z += other[2]

    # Subtracting
    def __sub__(self, other) -> 'Direction':
        return Direction(self.x - other[0], self.y - other[1], self.z - other[2])
    
    def __rsub__(self, other) -> 'Direction':
        return Direction(other[0] - self.x, other[1] - self.y, other[2] - self.z)
    
    def __isub__(self, other) -> 'Direction':
        self.x -= other[0]
        self.y -= other[1]
        self.z -= other[2]

    # Multiplication
    def __mul__(self, value : int) -> 'Direction':
        return Direction(self.x * value, self.y * value, self.z * value)
    
    def __rmul__(self, value : int) -> 'Direction':
        return Direction(value * self.x, value * self.y, value * self.z)
    
    # Turns
    def opposite(self) -> 'Direction':
        return -self
    
    def right(self) -> 'Direction':
        return Direction(-self.z, self.y, self.x)
    
    def left(self) -> 'Direction':
        return Direction(self.z, self.y, -self.x)
    
    # Utility
    def __hash__(self):
        return hash(tuple(self))
    
    def to_2D(self) -> Direction2D:
        return Direction2D(self.x, self.z)
    
    # Display
    def __repr__(self) -> str:
        return f'Dir({self.x}, {self.y}, {self.z})'

    def text(self) -> str:
        if self == Directions.North:
            return 'north'
        if self == Directions.South:
            return 'south'
        if self == Directions.East:
            return 'east'
        if self == Directions.West:
            return 'west'
        if self == Directions.Up:
            return 'up'
        if self == Directions.Down:
            return 'down'
        
        raise ValueError(f'Direction {self} can\'t be converted to text')

class Directions2D:
    Zero = Direction2D(0, 0)

    XPlus = Direction2D(1, 0)
    XMinus = Direction2D(-1, 0)
    ZPlus = Direction2D(0, 1)
    ZMinus = Direction2D(0, -1)

    East = XPlus
    West = XMinus
    South = ZPlus
    North = ZMinus

    Northeast = North + East
    Northwest = North + West
    Southeast = South + East
    Southwest = South + West

    Cardinal = [North, East, South, West]
    Diagonals = [Northeast, Northwest, Southeast, Southwest]
    All8 = Cardinal + Diagonals

class Directions:
    Zero = Direction(0, 0, 0)

    XPlus = Direction(1, 0, 0)
    XMinus = Direction(-1, 0, 0)
    YPlus = Direction(0, 1, 0)
    YMinus = Direction(0, -1, 0)
    ZPlus = Direction(0, 0, 1)
    ZMinus = Direction(0, 0, -1)
    
    East = XPlus
    West = XMinus
    Up = YPlus
    Down = YMinus
    South = ZPlus
    North = ZMinus

    Northeast = North + East
    Northwest = North + West
    Southeast = South + East
    Southwest = South + West

    Cardinal = [North, East, South, West]
    Diagonals = [Northeast, Northwest, Southeast, Southwest]
    Orthoginal = Cardinal + [Up, Down]
    All8 = Cardinal + Diagonals
    Omni = [Direction(*(i % 3 - 1, (i // 3) % 3 - 1, i // 9 - 1)) for i in range(1, 27)]