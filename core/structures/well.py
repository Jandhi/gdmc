
from random import randint, seed
from gdpc import Editor, Block
from core.structures.legacy_directions import north, east, west, south, to_text, opposite
from gdpc.vector_tools import ivec3
from core.utils.setblock import place_block

class Well:
    name = 'Well'
    origin = ivec3(0,0,0)

    def __init__(self, point: ivec3) -> None:
        self.origin = point

    def build(self, editor: Editor):

        x = self.origin.x
        y = self.origin.y
        z = self.origin.z

        cx, cz = x + 3, z + 3
        
        #surrounding the water hole with wall
        for dx, dz in ((-1,0), (0,-1), (0,1), (1,0)):
            for dy in range(-2, 0):
                editor.placeBlock((dx+cx, y+dy, dz+cz), Block('minecraft:cobblestone'))

        #bottom block of well
        editor.placeBlock((cx, y -3, cz), Block('minecraft:cobblestone'))

        #well sides
        for dx, dz, dir in ((-1,0, west), (0,-1, north), (0,1, south), 
            (1,0, east), (1,1, east), (1,-1, east), 
            (-1,1, west), (-1,-1, west)
        ):  
            editor.placeBlock((dx+cx, y, dz+cz), Block(f'minecraft:cobblestone_stairs[facing={to_text(dir)},waterlogged=true]'))

        #corners
        for dx, dz in ((1,1), (1,-1), (-1,1), (-1,-1)):
            for dy in range(1, 4):
                if dy == 3:
                    block = Block('minecraft:cobblestone')
                else:
                    block = Block('minecraft:cobblestone_wall')
                editor.placeBlock((dx+cx, y+dy, dz+cz), block)

        #add water
        for dy in range(-2, 1):
            editor.placeBlock((cx, y+dy, cz), Block('minecraft:water'))

        #roof
        for dx, dz in (
                (2, 1), (2, -1),
                (1, 2),  (-1, 2),
                (-2, 1), (-2, -1),
                (1, -2), (-1, -2)
            ):
            editor.placeBlock((cx+dx, y+3, cz+dz), Block('minecraft:cobblestone_slab'))

        for dx, dz in ((-1,0), (0,-1), (0,1), (1,0)):
            editor.placeBlock((cx+dx, y+3, cz+dz), Block('minecraft:cobblestone_slab[type=top]'))

        editor.placeBlock((cx, y+4, cz), Block('minecraft:cobblestone_slab'))

        for dx, dz, dir in (
            (2, 0, east), (0, 2, south), (-2, 0, west), (0, -2, north)
            ):
            editor.placeBlock((dx+cx, y + 3, dz+cz), Block(f'minecraft:cobblestone_stairs[facing={to_text(opposite(dir))}]'))

        #chain and bucket
        block = Block('minecraft:chain')
        editor.placeBlock((cx, y + 2, cz), block)
        editor.placeBlock((cx, y + 3, cz), block)
        seed()
        a = randint(0,3)
        if a == 0:
            block = Block(f'minecraft:cauldron')
        else:
            block = Block(f'minecraft:water_cauldron[level={a}]')
        editor.placeBlock((cx, y + 1, cz), block)

        #random bucket
        seed()
        pos = randint(0,15)
        places = [(2, 1), (2, 0), (2, -1), (2, 2), 
            (1, 2), (0, 2), (-1, 2), (2, -2), 
            (-2, 1), (-2, 0), (-2, -1), (-2, 2), 
            (1, -2), (0, -2), (-1, -2), (-2, -2)]
        dx, dz = places[pos]
        block = 'player_head{SkullOwner:{Id:[I;-1748225354,-1609481680,-1708141395,1310692466],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjAyYzk5Y2I5NjY3NDZiMGUzZDE2OTczZmMyY2RjZTRlNDBiODdhODZjMDVlMGE1MDIxZjM1YTAxOTJhNDBiMiJ9fX0="}]}}}'
        place_block(block, editor, ivec3(cx+dx, y, cz+dz))