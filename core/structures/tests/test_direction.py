# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\structures\\tests')

from core.structures.directions import Directions

assert(Directions.North - Directions.North == Directions.Zero)
assert(Directions.North * 0 == Directions.Zero)
assert(Directions.North * 1 != Directions.North * 2)
assert(Directions.North + Directions.West == Directions.Northwest)
assert(Directions.North == Directions.South.opposite())
assert(Directions.North == -Directions.South)

assert(Directions.North.text() == 'north')


assert(abs(Directions.Northwest) == Directions.Southeast)

assert(Directions.North.right() == Directions.East)
assert(Directions.East.right() == Directions.South)
assert(Directions.South.right() == Directions.West)
assert(Directions.West.right() == Directions.North)

assert(Directions.North.left() == Directions.East.opposite())
assert(Directions.East.left() == Directions.South.opposite())
assert(Directions.South.left() == Directions.West.opposite())
assert(Directions.West.left() == Directions.North.opposite())

assert(len(Directions.Omni) == 26)
assert(len(set(Directions.Omni)) == 26)

assert(Directions.North.to_2D().to_3D() == Directions.East.left())