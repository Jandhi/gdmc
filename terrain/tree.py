from gdpc import Editor, Block
from gdpc.vector_tools import ivec3
from random import seed
from random import randint
from core.noise.rng import RNG
from core.noise.random import choose_weighted

def place_block(editor: Editor, x: int, y: int, z: int, block: Block, chance: int=100):
        seed()
        if chance!=100:
            a = randint(1,100)
            if a<=chance:
                editor.placeBlock((x, y, z), Block(block))
            else:
                pass
        else:
            editor.placeBlock((x, y, z), Block(block))

def generate_tree(type: str, point: ivec3, editor: Editor, palette: dict):
    rng = RNG(randint(0,1000))
    wood = choose_weighted(rng.value(), palette["wood"])
    leaf = choose_weighted(rng.value(), palette["leaves"])
    if type == 'medium_pine':
        generate_medium_pine(point, editor, wood, leaf, 95)
    elif type == 'small_pine':
        generate_small_pine(point, editor, wood, leaf)
    elif type == 'large_pine':
        generate_large_pine(point, editor, wood, leaf, 95)
    elif type == 'mega_pine':
        generate_mega_pine(point, editor, wood, leaf, 95)
    elif type == 'small_birch':
        generate_small_birch(point, editor, wood, leaf, 98)
    elif type == 'medium_birch':
        generate_medium_birch(point, editor, wood, leaf, 96)
    elif type == 'large_birch':
        generate_large_birch(point, editor, wood, leaf, 95)
    elif type == 'mega_birch':
        generate_mega_birch(point, editor, wood, leaf, 93)
    elif type == 'small_hedge':
        generate_small_hedge(point, editor, wood, leaf)
    elif type == 'medium_hedge':
        generate_medium_hedge(point, editor, wood, leaf)
    elif type == 'large_hedge':
        generate_large_hedge(point, editor, wood, leaf)
    elif type == 'mega_hedge':
        generate_mega_hedge(point, editor, wood, leaf, 98)
    elif type == 'small_baobab':
        generate_small_baobab(point, editor, wood, leaf)
    elif type == 'medium_baobab':
        generate_medium_baobab(point, editor, wood, leaf)
    elif type == 'large_baobab':
        generate_large_baobab(point, editor, wood, leaf)
    elif type == 'small_oak':
        generate_small_oak(point, editor, wood, leaf)
    elif type == 'medium_oak':
        generate_medium_oak(point, editor, wood, leaf)
    elif type == 'large_oak':
        generate_large_oak(point, editor, wood, leaf)
    elif type == 'mega_oak':
        generate_mega_oak(point, editor, wood, leaf, 96)
    elif type == 'small_jungle':
        generate_small_jungle(point, editor, wood, leaf)
    elif type == 'medium_jungle':
        generate_medium_jungle(point, editor, wood, leaf)
    elif type == 'large_jungle':
        generate_large_jungle(point, editor, wood, leaf)
    elif type == 'mega_jungle':
        generate_mega_jungle(point, editor, wood, leaf)

def generate_small_pine(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()

    height = randint(5,7)+y0

    for y in range (y0,height+2):
        if y == height+1:
            place_block(editor, x0, y, z0, Block(leaf), leaf_chance)
            continue
        place_block(editor, x0, y, z0, Block(wood))
        if y%2 == height%2 and y > y0+1:
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
        elif y == height-1:
            place_block(editor, x0+1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
        elif y%2 == (height-1)%2 and y>y0:
            place_block(editor, x0+2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
            
def generate_medium_pine(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(8,13)+y0

    for y in range (y0,height+2):
        if y == height+1:
            place_block(editor, x0, y, z0, Block(leaf), leaf_chance)
            continue
        place_block(editor, x0, y, z0, Block(wood))
        if y == height:
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
        elif y == height-1:
            place_block(editor, x0+2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-2, Block(leaf), leaf_chance)
        elif y%2 == height%2 and y > y0+2:
            place_block(editor, x0+2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)

        elif y%2 == (height-1)%2 and y>y0+1:
            place_block(editor, x0+2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+3, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-3, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+3, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-3, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0-2, Block(leaf), leaf_chance)

def generate_large_pine(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(14,21)+y0

    for y in range (y0,height+3):
        if y == height+1:
            place_block(editor, x0, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
            continue
        elif y == height+2:
            place_block(editor, x0, y, z0, Block(leaf), leaf_chance)
            continue
        place_block(editor, x0, y, z0, Block(wood))
        if y == height:
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
        elif y%3 == (height-1)%3 and y > y0+5:
            place_block(editor, x0+2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
        elif y%3 == (height-2)%3 and y > y0+4:
            place_block(editor, x0+2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+3, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-3, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+3, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-3, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0-2, Block(leaf), leaf_chance)

        elif y%3 == height%3 and y>y0+3:
            place_block(editor, x0+2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+3, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-3, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+3, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-3, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+3, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-3, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+3, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-3, Block(leaf), leaf_chance)
            place_block(editor, x0+3, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0-3, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0+3, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0-3, Block(leaf), leaf_chance)
            place_block(editor, x0+3, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-3, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+3, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-3, Block(leaf), leaf_chance)
            place_block(editor, x0+3, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0-3, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0+3, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0-3, Block(leaf), leaf_chance)
            place_block(editor, x0+4, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-4, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+4, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-4, Block(leaf), leaf_chance)

def generate_mega_pine(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    generate_large_pine(point, editor, wood, leaf, leaf_chance)
    x0, y0, z0 = point.x, point.y, point.z
    new_point = ivec3(x0+1, y0, z0)
    generate_large_pine(new_point, editor, wood, leaf, leaf_chance)
    new_point = ivec3(x0+1, y0, z0+1)
    generate_large_pine(new_point, editor, wood, leaf, leaf_chance)
    new_point = ivec3(x0, y0, z0+1)
    generate_large_pine(new_point, editor, wood, leaf, leaf_chance)

def generate_small_birch(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(5,9)+y0

    for y in range (y0,height+3):
        if y >= height:
            place_block(editor, x0, y, z0, Block(leaf), leaf_chance)
        else:
            place_block(editor, x0, y, z0, Block(wood))
        if y==int((height-y0)/2+y0)-1 or y==height+1:
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
        elif y > int((height-y0)/2+y0)-1 and y < height+2:
            place_block(editor, x0+1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)

def generate_medium_birch(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(10,16)+y0
    branch_num = randint(2,5)
    branches = []
    branches.append([x0, height, z0])
    for y in range (y0,height): #tree stem
        place_block(editor, x0, y, z0, Block(wood))
        if y == y0:
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0+1, y, z0, Block(wood))
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0-1, y, z0, Block(wood))
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0, y, z0+1, Block(wood))
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0, y, z0-1, Block(wood))

    
    for a in range (0, branch_num):
        branch_height = randint(int((height-y0)/2+y0)+2, height-1)
        branch_pos = randint(1, 16)
        if branch_pos == 1:
            branches.append([x0+2,branch_height,z0])
            place_block(editor, x0+2, branch_height, z0, Block(wood))
            place_block(editor, x0+2, branch_height-1, z0, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0, Block(wood))
        elif branch_pos == 2:
            branches.append([x0+2,branch_height,z0+1])
            place_block(editor, x0+2, branch_height, z0+1, Block(wood))
            place_block(editor, x0+2,branch_height-1,z0+1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-2,z0+1, Block(wood))
            else:
                place_block(editor, x0+1,branch_height-2,z0, Block(wood))
        elif branch_pos == 3:
            branches.append([x0+2,branch_height,z0+2])
            place_block(editor, x0+2,branch_height,z0+2, Block(wood))
            place_block(editor, x0+2,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0+1,branch_height-2,z0+1, Block(wood))
        elif branch_pos == 4:
            branches.append([x0+2,branch_height,z0-1])
            place_block(editor, x0+2, branch_height, z0-1, Block(wood))
            place_block(editor, x0+2, branch_height-1, z0-1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-2,z0-1, Block(wood))
            else:
                place_block(editor, x0+1,branch_height-2,z0, Block(wood))
        elif branch_pos == 5:
            branches.append([x0+2,branch_height,z0-2])
            place_block(editor, x0+2, branch_height, z0-2, Block(wood))
            place_block(editor, x0+2, branch_height-1, z0-2, Block(wood))
            place_block(editor, x0+1,branch_height-2,z0-1, Block(wood))
        elif branch_pos == 6:
            branches.append([x0-2,branch_height,z0])
            place_block(editor, x0-2, branch_height, z0, Block(wood))
            place_block(editor, x0-2, branch_height-1, z0, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0, Block(wood))
        elif branch_pos == 7:
            branches.append([x0-2,branch_height,z0+1])
            place_block(editor, x0-2,branch_height,z0+1, Block(wood))
            place_block(editor, x0-2,branch_height-1,z0+1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-2,z0+1, Block(wood))
            else:
                place_block(editor, x0-1,branch_height-2,z0, Block(wood))
        elif branch_pos == 8:
            branches.append([x0-2,branch_height,z0+2])
            place_block(editor, x0-2,branch_height,z0+2, Block(wood))
            place_block(editor, x0-2,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0-1,branch_height-2,z0+1, Block(wood))
        elif branch_pos == 9:
            branches.append([x0-2,branch_height,z0-1])
            place_block(editor, x0-2, branch_height, z0-1, Block(wood))
            place_block(editor, x0-2, branch_height-1, z0-1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-2,z0-1, Block(wood))
            else:
                place_block(editor, x0-1,branch_height-2,z0, Block(wood))
        elif branch_pos == 10:
            branches.append([x0-2,branch_height,z0-2])
            place_block(editor, x0-2, branch_height, z0-2, Block(wood))
            place_block(editor, x0-2, branch_height-1, z0-2, Block(wood))
            place_block(editor, x0-1,branch_height-2,z0-1, Block(wood))
        elif branch_pos == 11:
            branches.append([x0+1,branch_height,z0-2])
            place_block(editor, x0+1, branch_height, z0-2, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0-2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-2,z0-1, Block(wood))
            else:
                place_block(editor, x0,branch_height-2,z0-1, Block(wood))
        elif branch_pos == 12:
            branches.append([x0,branch_height,z0-2])
            place_block(editor, x0, branch_height, z0-2, Block(wood))
            place_block(editor, x0, branch_height-1, z0-2, Block(wood))
            place_block(editor, x0, branch_height-2, z0-1, Block(wood))
        elif branch_pos == 13:
            branches.append([x0-1,branch_height,z0-2])
            place_block(editor, x0-1, branch_height, z0-2, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0-2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-2,z0-1, Block(wood))
            else:
                place_block(editor, x0,branch_height-2,z0-1, Block(wood))
        elif branch_pos == 14:
            branches.append([x0+1,branch_height,z0+2])
            place_block(editor, x0+1, branch_height, z0+2, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0+2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-2,z0+1, Block(wood))
            else:
                place_block(editor, x0,branch_height-2,z0+1, Block(wood))
        elif branch_pos == 15:
            branches.append([x0,branch_height,z0+2])
            place_block(editor, x0, branch_height, z0+2, Block(wood))
            place_block(editor, x0, branch_height-1, z0+2, Block(wood))
            place_block(editor, x0, branch_height-2, z0+1, Block(wood))
        elif branch_pos == 16:
            branches.append([x0-1,branch_height,z0+2])
            place_block(editor, x0-1, branch_height, z0+2, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0+2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-2,z0+1, Block(wood))
            else:
                place_block(editor, x0,branch_height-2,z0+1, Block(wood))

    for branch in branches:
        x1, y1, z1 = branch[0], branch[1], branch[2]

        place_block(editor, x1, y1+3, z1, Block(leaf), leaf_chance)

        place_block(editor, x1, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1-1, Block(leaf), leaf_chance)

        place_block(editor, x1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-1, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-1, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1-1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1-1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1-1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1-1, z1-1, Block(leaf), leaf_chance)

def generate_large_birch(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(16,23)+y0
    branch_num = randint(3,7)
    branches = []
    branches.append([x0, height, z0])
    for y in range (y0,height): #tree stem
        place_block(editor, x0, y, z0, Block(wood))
        if y == y0:
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0+1, y, z0, Block(wood))
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0-1, y, z0, Block(wood))
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0, y, z0+1, Block(wood))
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0, y, z0-1, Block(wood))

    
    for a in range (0, branch_num):
        branch_height = randint(int((height-y0)/2+y0)+4, height-1)
        branch_pos = randint(1, 24)
        if branch_pos == 1:
            branches.append([x0+3,branch_height,z0])
            place_block(editor, x0+3, branch_height, z0, Block(wood))
            place_block(editor, x0+3, branch_height-1, z0, Block(wood))
            place_block(editor, x0+3, branch_height-2, z0, Block(wood))
            place_block(editor, x0+2, branch_height-3, z0, Block(wood))
            place_block(editor, x0+1, branch_height-4, z0, Block(wood))
        elif branch_pos == 2:
            branches.append([x0+3,branch_height,z0+1])
            place_block(editor, x0+3,branch_height,z0+1, Block(wood))
            place_block(editor, x0+3,branch_height-1,z0+1, Block(wood))
            place_block(editor, x0+3,branch_height-2,z0+1, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+2,branch_height-3,z0+1, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0+1, Block(wood))
            elif b==2:
                place_block(editor, x0+2,branch_height-3,z0+1, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-3,z0, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0, Block(wood))
        elif branch_pos == 3:
            branches.append([x0+3,branch_height,z0+3])
            place_block(editor, x0+3, branch_height, z0+3, Block(wood))
            place_block(editor, x0+3, branch_height-1, z0+3, Block(wood))
            place_block(editor, x0+3, branch_height-2, z0+3, Block(wood))
            place_block(editor, x0+2, branch_height-3, z0+2, Block(wood))
            place_block(editor, x0+1, branch_height-4, z0+1, Block(wood))
        elif branch_pos == 4:
            branches.append([x0+3,branch_height,z0-1])
            place_block(editor, x0+3,branch_height,z0-1, Block(wood))
            place_block(editor, x0+3,branch_height-1,z0-1, Block(wood))
            place_block(editor, x0+3,branch_height-2,z0-1, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+2,branch_height-3,z0-1, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0-1, Block(wood))
            elif b==2:
                place_block(editor, x0+2,branch_height-3,z0-1, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-3,z0, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0, Block(wood))
        elif branch_pos == 5:
            branches.append([x0+3,branch_height,z0-3])
            place_block(editor, x0+3, branch_height, z0-3, Block(wood))
            place_block(editor, x0+3, branch_height-1, z0-3, Block(wood))
            place_block(editor, x0+3, branch_height-2, z0-3, Block(wood))
            place_block(editor, x0+2, branch_height-3, z0-2, Block(wood))
            place_block(editor, x0+1, branch_height-4, z0-1, Block(wood))
        elif branch_pos == 6:
            branches.append([x0-3,branch_height,z0])
            place_block(editor, x0-3, branch_height, z0, Block(wood))
            place_block(editor, x0-3, branch_height-1, z0, Block(wood))
            place_block(editor, x0-3, branch_height-2, z0, Block(wood))
            place_block(editor, x0-2, branch_height-3, z0, Block(wood))
            place_block(editor, x0-1, branch_height-4, z0, Block(wood))
        elif branch_pos == 7:
            branches.append([x0-3,branch_height,z0+1])
            place_block(editor, x0-3,branch_height,z0+1, Block(wood))
            place_block(editor, x0-3,branch_height-1,z0+1, Block(wood))
            place_block(editor, x0+-3,branch_height-2,z0+1, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-2,branch_height-3,z0+1, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0+1, Block(wood))
            elif b==2:
                place_block(editor, x0-2,branch_height-3,z0+1, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-3,z0, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0, Block(wood))
        elif branch_pos == 8:
            branches.append([x0-3,branch_height,z0+3])
            place_block(editor, x0-3, branch_height, z0+3, Block(wood))
            place_block(editor, x0-3, branch_height-1, z0+3, Block(wood))
            place_block(editor, x0-3, branch_height-2, z0+3, Block(wood))
            place_block(editor, x0-2, branch_height-3, z0+2, Block(wood))
            place_block(editor, x0-1, branch_height-4, z0+1, Block(wood))
        elif branch_pos == 9:
            branches.append([x0-3,branch_height,z0-1])
            place_block(editor, x0-3,branch_height,z0-1, Block(wood))
            place_block(editor, x0-3,branch_height-1,z0-1, Block(wood))
            place_block(editor, x0-3,branch_height-2,z0-1, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-2,branch_height-3,z0-1, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0-1, Block(wood))
            elif b==2:
                place_block(editor, x0-2,branch_height-3,z0-1, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-3,z0, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0, Block(wood))
        elif branch_pos == 10:
            branches.append([x0-3,branch_height,z0-3])
            place_block(editor, x0-3, branch_height, z0-3, Block(wood))
            place_block(editor, x0-3, branch_height-1, z0-3, Block(wood))
            place_block(editor, x0-3, branch_height-2, z0-3, Block(wood))
            place_block(editor, x0-2, branch_height-3, z0-2, Block(wood))
            place_block(editor, x0-1, branch_height-4, z0-1, Block(wood))
        elif branch_pos == 11:
            branches.append([x0+1,branch_height,z0-3])
            place_block(editor, x0+1, branch_height, z0-3, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0-3, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0-3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+1,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0-1, Block(wood))
            elif b==2:
                place_block(editor, x0+1,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0,branch_height-4,z0-1, Block(wood))
            else:
                place_block(editor, x0,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0,branch_height-4,z0-1, Block(wood))
        elif branch_pos == 12:
            branches.append([x0,branch_height,z0-3])
            place_block(editor, x0, branch_height, z0-3, Block(wood))
            place_block(editor, x0, branch_height-1, z0-3, Block(wood))
            place_block(editor, x0, branch_height-2, z0-3, Block(wood))
            place_block(editor, x0, branch_height-3, z0-2, Block(wood))
            place_block(editor, x0, branch_height-4, z0-1, Block(wood))
        elif branch_pos == 13:
            branches.append([x0+1,branch_height,z0-3])
            place_block(editor, x0-1, branch_height, z0-3, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0-3, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0-3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-1,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0-1, Block(wood))
            elif b==2:
                place_block(editor, x0-1,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0,branch_height-4,z0-1, Block(wood))
            else:
                place_block(editor, x0,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0,branch_height-4,z0-1, Block(wood))
        elif branch_pos == 14:
            branches.append([x0+1,branch_height,z0+3])
            place_block(editor, x0+1, branch_height, z0+3, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0+3, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0+3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+1,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0+1, Block(wood))
            elif b==2:
                place_block(editor, x0+1,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0,branch_height-4,z0+1, Block(wood))
            else:
                place_block(editor, x0,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0,branch_height-4,z0+1, Block(wood))
        elif branch_pos == 15:
            branches.append([x0,branch_height,z0+3])
            place_block(editor, x0, branch_height, z0+3, Block(wood))
            place_block(editor, x0, branch_height-1, z0+3, Block(wood))
            place_block(editor, x0, branch_height-2, z0+3, Block(wood))
            place_block(editor, x0, branch_height-3, z0+2, Block(wood))
            place_block(editor, x0, branch_height-4, z0+1, Block(wood))
        elif branch_pos == 16:
            branches.append([x0+1,branch_height,z0+3])
            place_block(editor, x0-1, branch_height, z0+3, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0+3, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0+3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-1,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0+1, Block(wood))
            elif b==2:
                place_block(editor, x0-1,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0,branch_height-4,z0+1, Block(wood))
            else:
                place_block(editor, x0,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0,branch_height-4,z0+1, Block(wood))
        elif branch_pos == 17:
            branches.append([x0+3,branch_height,z0+2])
            place_block(editor, x0+3,branch_height,z0+2, Block(wood))
            place_block(editor, x0+3,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0+3,branch_height-2,z0+2, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+2,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0+1, Block(wood))
            elif b==2:
                place_block(editor, x0+2,branch_height-3,z0+1, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0+1, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-3,z0+1, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0, Block(wood))
        elif branch_pos == 18:
            branches.append([x0+3,branch_height,z0-2])
            place_block(editor, x0+3,branch_height,z0-2, Block(wood))
            place_block(editor, x0+3,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0+3,branch_height-2,z0-2, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+2,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0-1, Block(wood))
            elif b==2:
                place_block(editor, x0+2,branch_height-3,z0-1, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0-1, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-3,z0-1, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0, Block(wood))
        elif branch_pos == 19:
            branches.append([x0-3,branch_height,z0+2])
            place_block(editor, x0-3,branch_height,z0+2, Block(wood))
            place_block(editor, x0-3,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0-3,branch_height-2,z0+2, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-2,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0+1, Block(wood))
            elif b==2:
                place_block(editor, x0-2,branch_height-3,z0+1, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0+1, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-3,z0+1, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0, Block(wood))
        elif branch_pos == 20:
            branches.append([x0-3,branch_height,z0-2])
            place_block(editor, x0-3,branch_height,z0-2, Block(wood))
            place_block(editor, x0-3,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0-3,branch_height-2,z0-2, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-2,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0-1, Block(wood))
            elif b==2:
                place_block(editor, x0-2,branch_height-3,z0-1, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0-1, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-3,z0-1, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0, Block(wood))
        elif branch_pos == 21:
            branches.append([x0+2,branch_height,z0+3])
            place_block(editor, x0+2,branch_height,z0+3, Block(wood))
            place_block(editor, x0+2,branch_height-1,z0+3, Block(wood))
            place_block(editor, x0+2,branch_height-2,z0+3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+2,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0+1, Block(wood))
            elif b==2:
                place_block(editor, x0+1,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0+1, Block(wood))
            else:
                place_block(editor, x0+1,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0,branch_height-4,z0+1, Block(wood))
        elif branch_pos == 22:
            branches.append([x0-2,branch_height,z0+3])
            place_block(editor, x0-2,branch_height,z0+3, Block(wood))
            place_block(editor, x0-2,branch_height-1,z0+3, Block(wood))
            place_block(editor, x0-2,branch_height-2,z0+3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-2,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0+1, Block(wood))
            elif b==2:
                place_block(editor, x0-1,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0+1, Block(wood))
            else:
                place_block(editor, x0-1,branch_height-3,z0+2, Block(wood))
                place_block(editor, x0,branch_height-4,z0+1, Block(wood))
        elif branch_pos == 23:
            branches.append([x0+2,branch_height,z0-3])
            place_block(editor, x0+2,branch_height,z0-3, Block(wood))
            place_block(editor, x0+2,branch_height-1,z0-3, Block(wood))
            place_block(editor, x0+2,branch_height-2,z0-3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+2,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0-1, Block(wood))
            elif b==2:
                place_block(editor, x0+1,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0+1,branch_height-4,z0-1, Block(wood))
            else:
                place_block(editor, x0+1,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0,branch_height-4,z0-1, Block(wood))
        elif branch_pos == 24:
            branches.append([x0-2,branch_height,z0-3])
            place_block(editor, x0-2,branch_height,z0-3, Block(wood))
            place_block(editor, x0-2,branch_height-1,z0-3, Block(wood))
            place_block(editor, x0-2,branch_height-2,z0-3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-2,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0-1, Block(wood))
            elif b==2:
                place_block(editor, x0-1,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0-1,branch_height-4,z0-1, Block(wood))
            else:
                place_block(editor, x0-1,branch_height-3,z0-2, Block(wood))
                place_block(editor, x0,branch_height-4,z0-1, Block(wood))

    for branch in branches:
        x1, y1, z1 = branch[0], branch[1], branch[2]

        place_block(editor, x1, y1+4, z1, Block(leaf), leaf_chance)

        place_block(editor, x1, y1+3, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+3, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+3, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+3, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+3, z1-1, Block(leaf), leaf_chance)

        place_block(editor, x1, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+2, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+2, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+2, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+2, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1-2, Block(leaf), leaf_chance)

        place_block(editor, x1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1-2, Block(leaf), leaf_chance)
        
        place_block(editor, x1+1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-2, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1-1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1-1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1-1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1-1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1-1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1-1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1-1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1-1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1-2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1-2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1-2, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1-2, z1-1, Block(leaf), leaf_chance)
        
def generate_mega_birch(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    generate_large_birch(point, editor, wood, leaf, leaf_chance)
    x0, y0, z0 = point.x, point.y, point.z
    new_point = ivec3(x0+1, y0, z0)
    generate_large_birch(new_point, editor, wood, leaf, leaf_chance)
    new_point = ivec3(x0+1, y0, z0+1)
    generate_large_birch(new_point, editor, wood, leaf, leaf_chance)
    new_point = ivec3(x0, y0, z0+1)
    generate_large_birch(new_point, editor, wood, leaf, leaf_chance)

def generate_small_hedge(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(4,7)+y0

    for y in range (y0,height+2):
        if y == height+1:
            place_block(editor, x0, y, z0, Block(leaf), leaf_chance)
            continue
        else:
            place_block(editor, x0, y, z0, Block(wood))
        if y>y0:
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)

def generate_medium_hedge(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(8,13)+y0

    for y in range (y0,height+2):
        if y == height+1:
            place_block(editor, x0, y, z0, Block(leaf), leaf_chance)
            continue
        else:
            place_block(editor, x0, y, z0, Block(wood))
        if y>y0:
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
        if y>y0+2 and y<height-1:
            place_block(editor, x0+1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-1, Block(leaf), leaf_chance)

def generate_large_hedge(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(14,19)+y0

    for y in range (y0,height+2):
        if y == height+1:
            place_block(editor, x0, y, z0, Block(leaf), leaf_chance)
            continue
        else:
            place_block(editor, x0, y, z0, Block(wood))
        if y>y0:
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
        if y>y0+2 and y<height-1:
            place_block(editor, x0+1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-1, Block(leaf), leaf_chance)
        if y>y0+3 and y<height-2:
            place_block(editor, x0+2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-2, Block(leaf), leaf_chance)
        if y>y0+5 and y<height-4:
            place_block(editor, x0+2, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-2, Block(leaf), leaf_chance)

def generate_mega_hedge(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    generate_large_hedge(point, editor, wood, leaf, leaf_chance)
    x0, y0, z0 = point.x, point.y, point.z
    new_point = ivec3(x0+1, y0, z0)
    generate_large_hedge(new_point, editor, wood, leaf, leaf_chance)
    new_point = ivec3(x0+1, y0, z0+1)
    generate_large_hedge(new_point, editor, wood, leaf, leaf_chance)
    new_point = ivec3(x0, y0, z0+1)
    generate_large_hedge(new_point, editor, wood, leaf, leaf_chance)

def generate_small_baobab(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(12,19)+y0
    branches = []
    
    for y in range (y0,height+1): #tree stem
        place_block(editor, x0, y, z0, Block(wood))
        place_block(editor, x0+1, y, z0+1, Block(wood))
        place_block(editor, x0+1, y, z0, Block(wood))
        place_block(editor, x0, y, z0+1, Block(wood))

    main_branch_pos = randint(0,3)
    if main_branch_pos == 0: #main branch
        branches.append([x0, height+2, z0])
        place_block(editor, x0, height+1, z0, Block(wood))
        place_block(editor, x0, height+2, z0, Block(wood))
    elif main_branch_pos == 1:
        branches.append([x0, height+2, z0+1])
        place_block(editor, x0, height+1, z0+1, Block(wood))
        place_block(editor, x0, height+2, z0+1, Block(wood))
    elif main_branch_pos == 2:
        branches.append([x0+1, height+2, z0])
        place_block(editor, x0+1, height+1, z0, Block(wood))
        place_block(editor, x0+1, height+2, z0, Block(wood))
    else:
        branches.append([x0+1, height+2, z0+1])
        place_block(editor, x0+1, height+1, z0+1, Block(wood))
        place_block(editor, x0+1, height+2, z0+1, Block(wood))

    # random branch generation, 1 random branch for each quadrant
    branch_height = height
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0-2,branch_height+1,z0])
        place_block(editor, x0-2, branch_height+1, z0, Block(wood))
        place_block(editor, x0-1, branch_height, z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-2,branch_height+1,z0-1])
        place_block(editor, x0-2, branch_height+1, z0-1, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0-1,branch_height,z0-1, Block(wood))
        else:
            place_block(editor, x0-1,branch_height,z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-2,branch_height+1,z0-2])
        place_block(editor, x0-2, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0-1,branch_height,z0-1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0-1,branch_height+1,z0-2])
        place_block(editor, x0-1, branch_height+1, z0-2, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0-1,branch_height,z0-1, Block(wood))
        else:
            place_block(editor, x0,branch_height,z0-1, Block(wood))
    elif branch_pos == 5:
        branches.append([x0,branch_height+1,z0-2])
        place_block(editor, x0, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0, branch_height, z0-1, Block(wood))

    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0-2,branch_height+1,z0+1])
        place_block(editor, x0-2,branch_height+1,z0+1, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0-1,branch_height,z0+1, Block(wood))
        else:
            place_block(editor, x0-1,branch_height,z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-2,branch_height+1,z0+2])
        place_block(editor, x0-2,branch_height+1,z0+2, Block(wood))
        place_block(editor, x0-1,branch_height,z0+1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-2,branch_height+1,z0+3])
        place_block(editor, x0-2,branch_height+1,z0+3, Block(wood))
        place_block(editor, x0-1,branch_height,z0+2, Block(wood))
    elif branch_pos == 4:
        branches.append([x0,branch_height+1,z0+3])
        place_block(editor, x0, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0, branch_height, z0+2, Block(wood))
    elif branch_pos == 5:
        branches.append([x0-1,branch_height+1,z0+3])
        place_block(editor, x0-1, branch_height+1, z0+3, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0-1,branch_height,z0+2, Block(wood))
        else:
            place_block(editor, x0,branch_height,z0+2, Block(wood))

    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0+1,branch_height+1,z0+3])
        place_block(editor, x0+1, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0+1,branch_height,z0+2, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+2,branch_height+1,z0+3])
        place_block(editor, x0+2,branch_height+1,z0+3, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0+1,branch_height,z0+2, Block(wood))
        else:
            place_block(editor, x0+2,branch_height,z0+2, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+3,branch_height+1,z0+3])
        place_block(editor, x0+3,branch_height+1,z0+3, Block(wood))
        place_block(editor, x0+2,branch_height,z0+2, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+3,branch_height+1,z0+2])
        place_block(editor, x0+3,branch_height+1,z0+2, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0+2, branch_height, z0+1, Block(wood))
        else:
            place_block(editor, x0+2,branch_height,z0+2, Block(wood))
    elif branch_pos == 5:
        branches.append([x0+3,branch_height+1,z0+1])
        place_block(editor, x0+3,branch_height+1,z0+1, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0+2, branch_height, z0+1, Block(wood))
        else:
            place_block(editor, x0+2, branch_height, z0+1, Block(wood))

    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0+3,branch_height+1,z0])
        place_block(editor, x0+3, branch_height+1, z0, Block(wood))
        place_block(editor, x0+2, branch_height, z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+3,branch_height+1,z0-1])
        place_block(editor, x0+3, branch_height+1, z0-1, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0+2,branch_height,z0-1, Block(wood))
        else:
            place_block(editor, x0+2,branch_height,z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+3,branch_height+1,z0-2])
        place_block(editor, x0+3, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0+2,branch_height,z0-1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+2,branch_height+1,z0-2])
        place_block(editor, x0+2, branch_height+1, z0-2, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0+1,branch_height,z0-1, Block(wood))
        else:
            place_block(editor, x0+2,branch_height,z0-1, Block(wood))
    elif branch_pos == 5:
        branches.append([x0+1,branch_height+1,z0-2])
        place_block(editor, x0+1, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0+1,branch_height,z0-1, Block(wood))

    for branch in branches:
        x1, y1, z1 = branch[0], branch[1], branch[2]

        place_block(editor, x1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-1, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-2, Block(leaf), leaf_chance)

def generate_medium_baobab(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(18,25)+y0
    branches = []
    
    for y in range (y0,height+1): #tree stem
        place_block(editor, x0, y, z0, Block(wood))
        place_block(editor, x0+1, y, z0+1, Block(wood))
        place_block(editor, x0+1, y, z0, Block(wood))
        place_block(editor, x0, y, z0+1, Block(wood))
        place_block(editor, x0-1, y, z0, Block(wood))
        place_block(editor, x0+1, y, z0+2, Block(wood))
        place_block(editor, x0+2, y, z0, Block(wood))
        place_block(editor, x0, y, z0+2, Block(wood))
        place_block(editor, x0, y, z0-1, Block(wood))
        place_block(editor, x0+2, y, z0+1, Block(wood))
        place_block(editor, x0+1, y, z0-1, Block(wood))
        place_block(editor, x0-1, y, z0+1, Block(wood))

    #main branch/top
    place_block(editor, x0, height+1, z0, Block(wood))
    place_block(editor, x0+1, height+1, z0, Block(wood))
    place_block(editor, x0+1, height+1, z0+1, Block(wood))
    place_block(editor, x0, height+1, z0+1, Block(wood))
    place_block(editor, x0, height+2, z0, Block(wood))
    place_block(editor, x0+1, height+2, z0, Block(wood))
    place_block(editor, x0+1, height+2, z0+1, Block(wood))
    place_block(editor, x0, height+2, z0+1, Block(wood))
    place_block(editor, x0, height+3, z0, Block(wood))
    place_block(editor, x0+1, height+3, z0, Block(wood))
    place_block(editor, x0+1, height+3, z0+1, Block(wood))
    place_block(editor, x0, height+3, z0+1, Block(wood))

    #main branch leaves
    place_block(editor, x0, height+4, z0, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+4, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+4, z0, Block(leaf), leaf_chance)
    place_block(editor, x0, height+4, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+4, z0, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+4, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+4, z0, Block(leaf), leaf_chance)
    place_block(editor, x0, height+4, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0, height+4, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+4, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+4, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+4, z0+1, Block(leaf), leaf_chance)

    place_block(editor, x0-1, height+3, z0, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+3, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+3, z0, Block(leaf), leaf_chance)
    place_block(editor, x0, height+3, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0, height+3, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+3, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+3, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+3, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+3, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0, height+3, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+3, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+3, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+3, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+3, z0, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+3, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+3, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+3, z0+3, Block(leaf), leaf_chance)
    place_block(editor, x0, height+3, z0+3, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+3, z0+3, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+3, z0+3, Block(leaf), leaf_chance)
    place_block(editor, x0+3, height+3, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0+3, height+3, z0, Block(leaf), leaf_chance)
    place_block(editor, x0+3, height+3, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0+3, height+3, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+3, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+3, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+3, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+3, z0+2, Block(leaf), leaf_chance)

    # random branch generation, 1 random branch for each quadrant
    branch_height = randint(height, height+1)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0-3,branch_height+1,z0-3])
        place_block(editor, x0-3, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0-2, branch_height, z0-2, Block(wood))
        place_block(editor, x0-1, branch_height, z0-1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-4,branch_height+1,z0-3])
        place_block(editor, x0-4, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0-3, branch_height, z0-2, Block(wood))
        place_block(editor, x0-2, branch_height, z0-1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-4,branch_height+1,z0-2])
        place_block(editor, x0-4, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0-3, branch_height, z0-2, Block(wood))
        place_block(editor, x0-2, branch_height, z0-1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0-3,branch_height+1,z0-4])
        place_block(editor, x0-3, branch_height+1, z0-4, Block(wood))
        place_block(editor, x0-2, branch_height, z0-3, Block(wood))
        place_block(editor, x0-1, branch_height, z0-2, Block(wood))
    elif branch_pos == 5:
        branches.append([x0-2,branch_height+1,z0-4])
        place_block(editor, x0-2, branch_height+1, z0-4, Block(wood))
        place_block(editor, x0-2, branch_height, z0-3, Block(wood))
        place_block(editor, x0-1, branch_height, z0-2, Block(wood))
    branch_height = randint(height, height+1)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0-3,branch_height+1,z0+4])
        place_block(editor, x0-3, branch_height+1, z0+4, Block(wood))
        place_block(editor, x0-2, branch_height, z0+3, Block(wood))
        place_block(editor, x0-1, branch_height, z0+2, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-4,branch_height+1,z0+4])
        place_block(editor, x0-4, branch_height+1, z0+4, Block(wood))
        place_block(editor, x0-3, branch_height, z0+3, Block(wood))
        place_block(editor, x0-2, branch_height, z0+2, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-4,branch_height+1,z0+3])
        place_block(editor, x0-4, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0-3, branch_height, z0+3, Block(wood))
        place_block(editor, x0-2, branch_height, z0+2, Block(wood))
    elif branch_pos == 4:
        branches.append([x0-3,branch_height+1,z0+5])
        place_block(editor, x0-3, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0-2, branch_height, z0+4, Block(wood))
        place_block(editor, x0-1, branch_height, z0+3, Block(wood))
    elif branch_pos == 5:
        branches.append([x0-2,branch_height+1,z0+5])
        place_block(editor, x0-2, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0-2, branch_height, z0+4, Block(wood))
        place_block(editor, x0-1, branch_height, z0+3, Block(wood))
    branch_height = randint(height, height+1)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0+4,branch_height+1,z0-3])
        place_block(editor, x0+4, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0+3, branch_height, z0-2, Block(wood))
        place_block(editor, x0+2, branch_height, z0-1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+5,branch_height+1,z0-3])
        place_block(editor, x0+5, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0+4, branch_height, z0-2, Block(wood))
        place_block(editor, x0+3, branch_height, z0-1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+5,branch_height+1,z0-2])
        place_block(editor, x0+5, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0+4, branch_height, z0-2, Block(wood))
        place_block(editor, x0+3, branch_height, z0-1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+4,branch_height+1,z0-4])
        place_block(editor, x0+4, branch_height+1, z0-4, Block(wood))
        place_block(editor, x0+3, branch_height, z0-3, Block(wood))
        place_block(editor, x0+2, branch_height, z0-2, Block(wood))
    elif branch_pos == 5:
        branches.append([x0+3,branch_height+1,z0-4])
        place_block(editor, x0+3, branch_height+1, z0-4, Block(wood))
        place_block(editor, x0+3, branch_height, z0-3, Block(wood))
        place_block(editor, x0+2, branch_height, z0-2, Block(wood))
    branch_height = randint(height, height+1)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0+4,branch_height+1,z0+4])
        place_block(editor, x0+4, branch_height+1, z0+4, Block(wood))
        place_block(editor, x0+3, branch_height, z0+3, Block(wood))
        place_block(editor, x0+2, branch_height, z0+2, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+5,branch_height+1,z0+4])
        place_block(editor, x0+5, branch_height+1, z0+4, Block(wood))
        place_block(editor, x0+4, branch_height, z0+3, Block(wood))
        place_block(editor, x0+3, branch_height, z0+2, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+5,branch_height+1,z0+3])
        place_block(editor, x0+5, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0+4, branch_height, z0+3, Block(wood))
        place_block(editor, x0+3, branch_height, z0+2, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+4,branch_height+1,z0+5])
        place_block(editor, x0+4, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0+3, branch_height, z0+4, Block(wood))
        place_block(editor, x0+2, branch_height, z0+3, Block(wood))
    elif branch_pos == 5:
        branches.append([x0+3,branch_height+1,z0+5])
        place_block(editor, x0+3, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0+3, branch_height, z0+4, Block(wood))
        place_block(editor, x0+2, branch_height, z0+3, Block(wood))
    branch_height = randint(height, height+1)
    branch_pos = randint(1, 4)
    if branch_pos == 1:
        branches.append([x0-1,branch_height+1,z0-4])
        place_block(editor, x0-1, branch_height+1, z0-4, Block(wood))
        place_block(editor, x0, branch_height, z0-3, Block(wood))
        place_block(editor, x0, branch_height, z0-2, Block(wood))
    elif branch_pos == 2:
        branches.append([x0,branch_height+1,z0-4])
        place_block(editor, x0, branch_height+1, z0-4, Block(wood))
        place_block(editor, x0, branch_height, z0-3, Block(wood))
        place_block(editor, x0, branch_height, z0-2, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+1,branch_height+1,z0-4])
        place_block(editor, x0+1, branch_height+1, z0-4, Block(wood))
        place_block(editor, x0+1, branch_height, z0-3, Block(wood))
        place_block(editor, x0+1, branch_height, z0-2, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+2,branch_height+1,z0-4])
        place_block(editor, x0+2, branch_height+1, z0-4, Block(wood))
        place_block(editor, x0+1, branch_height, z0-3, Block(wood))
        place_block(editor, x0+1, branch_height, z0-2, Block(wood))
    branch_height = randint(height, height+1)
    branch_pos = randint(1, 4)
    if branch_pos == 1:
        branches.append([x0-1,branch_height+1,z0+5])
        place_block(editor, x0-1, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0, branch_height, z0+4, Block(wood))
        place_block(editor, x0, branch_height, z0+3, Block(wood))
    elif branch_pos == 2:
        branches.append([x0,branch_height+1,z0+5])
        place_block(editor, x0, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0, branch_height, z0+4, Block(wood))
        place_block(editor, x0, branch_height, z0+3, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+1,branch_height+1,z0+5])
        place_block(editor, x0+1, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0+1, branch_height, z0+4, Block(wood))
        place_block(editor, x0+1, branch_height, z0+3, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+2,branch_height+1,z0+5])
        place_block(editor, x0+2, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0+1, branch_height, z0+4, Block(wood))
        place_block(editor, x0+1, branch_height, z0+3, Block(wood))
    branch_height = randint(height, height+1)
    branch_pos = randint(1, 4)
    if branch_pos == 1:
        branches.append([x0-4,branch_height+1,z0-1])
        place_block(editor, x0-4, branch_height+1, z0-1, Block(wood))
        place_block(editor, x0-3, branch_height, z0, Block(wood))
        place_block(editor, x0-2, branch_height, z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-4,branch_height+1,z0])
        place_block(editor, x0-4, branch_height+1, z0, Block(wood))
        place_block(editor, x0-3, branch_height, z0, Block(wood))
        place_block(editor, x0-2, branch_height, z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-4,branch_height+1,z0+1])
        place_block(editor, x0-4, branch_height+1, z0+1, Block(wood))
        place_block(editor, x0-3, branch_height, z0+1, Block(wood))
        place_block(editor, x0-2, branch_height, z0+1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0-4,branch_height+1,z0+2])
        place_block(editor, x0-4, branch_height+1, z0+2, Block(wood))
        place_block(editor, x0-3, branch_height, z0+1, Block(wood))
        place_block(editor, x0-2, branch_height, z0+1, Block(wood))
    branch_height = randint(height, height+1)
    branch_pos = randint(1, 4)
    if branch_pos == 1:
        branches.append([x0+5,branch_height+1,z0-1])
        place_block(editor, x0+5, branch_height+1, z0-1, Block(wood))
        place_block(editor, x0+4, branch_height, z0, Block(wood))
        place_block(editor, x0+3, branch_height, z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+5,branch_height+1,z0])
        place_block(editor, x0+5, branch_height+1, z0, Block(wood))
        place_block(editor, x0+4, branch_height, z0, Block(wood))
        place_block(editor, x0+3, branch_height, z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+5,branch_height+1,z0+1])
        place_block(editor, x0+5, branch_height+1, z0+1, Block(wood))
        place_block(editor, x0+4, branch_height, z0+1, Block(wood))
        place_block(editor, x0+3, branch_height, z0+1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+5,branch_height+1,z0+2])
        place_block(editor, x0+5, branch_height+1, z0+2, Block(wood))
        place_block(editor, x0+4, branch_height, z0+1, Block(wood))
        place_block(editor, x0+3, branch_height, z0+1, Block(wood))

    for branch in branches:
        x1, y1, z1 = branch[0], branch[1], branch[2]

        place_block(editor, x1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-1, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-2, Block(leaf), leaf_chance)

def generate_large_baobab(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(26,40)+y0
    branches = []
    
    for y in range (y0,height+1): #tree stem
        place_block(editor, x0, y, z0, Block(wood))
        place_block(editor, x0+1, y, z0+1, Block(wood))
        place_block(editor, x0+1, y, z0, Block(wood))
        place_block(editor, x0, y, z0+1, Block(wood))
        place_block(editor, x0-1, y, z0, Block(wood))
        place_block(editor, x0+1, y, z0+2, Block(wood))
        place_block(editor, x0+2, y, z0, Block(wood))
        place_block(editor, x0, y, z0+2, Block(wood))
        place_block(editor, x0, y, z0-1, Block(wood))
        place_block(editor, x0+2, y, z0+1, Block(wood))
        place_block(editor, x0+1, y, z0-1, Block(wood))
        place_block(editor, x0-1, y, z0+1, Block(wood))
        place_block(editor, x0+2, y, z0-1, Block(wood))
        place_block(editor, x0-1, y, z0-2, Block(wood))
        place_block(editor, x0, y, z0-2, Block(wood))
        place_block(editor, x0+1, y, z0-2, Block(wood))
        place_block(editor, x0-1, y, z0-1, Block(wood))
        place_block(editor, x0-2, y, z0-1, Block(wood))
        place_block(editor, x0-2, y, z0, Block(wood))
        place_block(editor, x0-2, y, z0+1, Block(wood))
        place_block(editor, x0-1, y, z0+2, Block(wood))

    #main branch/top
    place_block(editor, x0, height+1, z0, Block(wood))
    place_block(editor, x0+1, height+1, z0, Block(wood))
    place_block(editor, x0+1, height+1, z0+1, Block(wood))
    place_block(editor, x0, height+1, z0+1, Block(wood))
    place_block(editor, x0, height+1, z0-1, Block(wood))
    place_block(editor, x0-1, height+1, z0, Block(wood))
    place_block(editor, x0-1, height+1, z0+1, Block(wood))
    place_block(editor, x0+1, height+1, z0-1, Block(wood))
    place_block(editor, x0-1, height+1, z0-1, Block(wood))
    place_block(editor, x0, height+2, z0, Block(wood))
    place_block(editor, x0+1, height+2, z0, Block(wood))
    place_block(editor, x0+1, height+2, z0+1, Block(wood))
    place_block(editor, x0, height+2, z0+1, Block(wood))
    place_block(editor, x0, height+2, z0-1, Block(wood))
    place_block(editor, x0-1, height+2, z0, Block(wood))
    place_block(editor, x0-1, height+2, z0+1, Block(wood))
    place_block(editor, x0+1, height+2, z0-1, Block(wood))
    place_block(editor, x0-1, height+2, z0-1, Block(wood))
    place_block(editor, x0, height+3, z0, Block(wood))
    place_block(editor, x0+1, height+3, z0, Block(wood))
    place_block(editor, x0+1, height+3, z0+1, Block(wood))
    place_block(editor, x0, height+3, z0+1, Block(wood))
    place_block(editor, x0, height+3, z0-1, Block(wood))
    place_block(editor, x0-1, height+3, z0, Block(wood))
    place_block(editor, x0-1, height+3, z0+1, Block(wood))
    place_block(editor, x0+1, height+3, z0-1, Block(wood))
    place_block(editor, x0-1, height+3, z0-1, Block(wood))
    place_block(editor, x0, height+4, z0, Block(wood))
    place_block(editor, x0+1, height+4, z0, Block(wood))
    place_block(editor, x0+1, height+4, z0+1, Block(wood))
    place_block(editor, x0, height+4, z0+1, Block(wood))
    place_block(editor, x0, height+4, z0-1, Block(wood))
    place_block(editor, x0-1, height+4, z0, Block(wood))
    place_block(editor, x0-1, height+4, z0+1, Block(wood))
    place_block(editor, x0+1, height+4, z0-1, Block(wood))
    place_block(editor, x0-1, height+4, z0-1, Block(wood))


    #main branch leaves
    place_block(editor, x0, height+6, z0, Block(leaf), leaf_chance)
    place_block(editor, x0, height+6, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+6, z0, Block(leaf), leaf_chance)
    place_block(editor, x0, height+6, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+6, z0, Block(leaf), leaf_chance)

    place_block(editor, x0, height+5, z0, Block(leaf), leaf_chance)
    place_block(editor, x0, height+5, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+5, z0, Block(leaf), leaf_chance)
    place_block(editor, x0, height+5, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+5, z0, Block(leaf), leaf_chance)
    place_block(editor, x0, height+5, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+5, z0, Block(leaf), leaf_chance)
    place_block(editor, x0, height+5, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+5, z0, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+5, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+5, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+5, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+5, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+5, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+5, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+5, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+5, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+5, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+5, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+5, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+5, z0-1, Block(leaf), leaf_chance)

    place_block(editor, x0, height+4, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+4, z0, Block(leaf), leaf_chance)
    place_block(editor, x0, height+4, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+4, z0, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+4, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+4, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+4, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+4, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+4, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+4, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+4, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+4, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0, height+4, z0-3, Block(leaf), leaf_chance)
    place_block(editor, x0-3, height+4, z0, Block(leaf), leaf_chance)
    place_block(editor, x0, height+4, z0+3, Block(leaf), leaf_chance)
    place_block(editor, x0+3, height+4, z0, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+4, z0-3, Block(leaf), leaf_chance)
    place_block(editor, x0-3, height+4, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+4, z0+3, Block(leaf), leaf_chance)
    place_block(editor, x0+3, height+4, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+4, z0-3, Block(leaf), leaf_chance)
    place_block(editor, x0-3, height+4, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+4, z0+3, Block(leaf), leaf_chance)
    place_block(editor, x0+3, height+4, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0, height+4, z0-4, Block(leaf), leaf_chance)
    place_block(editor, x0-4, height+4, z0, Block(leaf), leaf_chance)
    place_block(editor, x0, height+4, z0+4, Block(leaf), leaf_chance)
    place_block(editor, x0+4, height+4, z0, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+4, z0-4, Block(leaf), leaf_chance)
    place_block(editor, x0-4, height+4, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0+1, height+4, z0+4, Block(leaf), leaf_chance)
    place_block(editor, x0+4, height+4, z0+1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+4, z0-4, Block(leaf), leaf_chance)
    place_block(editor, x0-4, height+4, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0-1, height+4, z0+4, Block(leaf), leaf_chance)
    place_block(editor, x0+4, height+4, z0-1, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+4, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+4, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+4, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+4, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+4, z0-3, Block(leaf), leaf_chance)
    place_block(editor, x0-2, height+4, z0+3, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+4, z0+3, Block(leaf), leaf_chance)
    place_block(editor, x0+2, height+4, z0-3, Block(leaf), leaf_chance)
    place_block(editor, x0-3, height+4, z0-2, Block(leaf), leaf_chance)
    place_block(editor, x0-3, height+4, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0+3, height+4, z0+2, Block(leaf), leaf_chance)
    place_block(editor, x0+3, height+4, z0-2, Block(leaf), leaf_chance)
    
    # random branch generation, 1 random branch for each quadrant
    branch_height = randint(height, height+2)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0-4,branch_height+1,z0-4])
        place_block(editor, x0-4, branch_height+1, z0-4, Block(wood))
        place_block(editor, x0-3, branch_height, z0-3, Block(wood))
        place_block(editor, x0-2, branch_height, z0-2, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-4,branch_height+1,z0-3])
        place_block(editor, x0-4, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0-3, branch_height, z0-2, Block(wood))
        place_block(editor, x0-2, branch_height, z0-1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-5,branch_height+1,z0-3])
        place_block(editor, x0-5, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0-4, branch_height, z0-2, Block(wood))
        place_block(editor, x0-3, branch_height, z0-2, Block(wood))
        place_block(editor, x0-2, branch_height, z0-1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0-3,branch_height+1,z0-4])
        place_block(editor, x0-3, branch_height+1, z0-4, Block(wood))
        place_block(editor, x0-2, branch_height, z0-3, Block(wood))
        place_block(editor, x0-1, branch_height, z0-2, Block(wood))
    elif branch_pos == 5:
        branches.append([x0-3,branch_height+1,z0-5])
        place_block(editor, x0-3, branch_height+1, z0-5, Block(wood))
        place_block(editor, x0-2, branch_height, z0-4, Block(wood))
        place_block(editor, x0-2, branch_height, z0-3, Block(wood))
        place_block(editor, x0-1, branch_height, z0-2, Block(wood))
    branch_height = randint(height, height+2)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0+4,branch_height+1,z0-4])
        place_block(editor, x0+4, branch_height+1, z0-4, Block(wood))
        place_block(editor, x0+3, branch_height, z0-3, Block(wood))
        place_block(editor, x0+2, branch_height, z0-2, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+4,branch_height+1,z0-3])
        place_block(editor, x0+4, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0+3, branch_height, z0-2, Block(wood))
        place_block(editor, x0+2, branch_height, z0-1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+5,branch_height+1,z0-3])
        place_block(editor, x0+5, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0+4, branch_height, z0-2, Block(wood))
        place_block(editor, x0+3, branch_height, z0-2, Block(wood))
        place_block(editor, x0+2, branch_height, z0-1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+3,branch_height+1,z0-4])
        place_block(editor, x0+3, branch_height+1, z0-4, Block(wood))
        place_block(editor, x0+2, branch_height, z0-3, Block(wood))
        place_block(editor, x0+1, branch_height, z0-2, Block(wood))
    elif branch_pos == 5:
        branches.append([x0+3,branch_height+1,z0-5])
        place_block(editor, x0+3, branch_height+1, z0-5, Block(wood))
        place_block(editor, x0+2, branch_height, z0-4, Block(wood))
        place_block(editor, x0+2, branch_height, z0-3, Block(wood))
        place_block(editor, x0+1, branch_height, z0-2, Block(wood))
    branch_height = randint(height, height+2)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0-4,branch_height+1,z0+4])
        place_block(editor, x0-4, branch_height+1, z0+4, Block(wood))
        place_block(editor, x0-3, branch_height, z0+3, Block(wood))
        place_block(editor, x0-2, branch_height, z0+2, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-4,branch_height+1,z0+3])
        place_block(editor, x0-4, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0-3, branch_height, z0+2, Block(wood))
        place_block(editor, x0-2, branch_height, z0+1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-5,branch_height+1,z0+3])
        place_block(editor, x0-5, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0-4, branch_height, z0+2, Block(wood))
        place_block(editor, x0-3, branch_height, z0+2, Block(wood))
        place_block(editor, x0-2, branch_height, z0+1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0-3,branch_height+1,z0+4])
        place_block(editor, x0-3, branch_height+1, z0+4, Block(wood))
        place_block(editor, x0-2, branch_height, z0+3, Block(wood))
        place_block(editor, x0-1, branch_height, z0+2, Block(wood))
    elif branch_pos == 5:
        branches.append([x0-3,branch_height+1,z0+5])
        place_block(editor, x0-3, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0-2, branch_height, z0+4, Block(wood))
        place_block(editor, x0-2, branch_height, z0+3, Block(wood))
        place_block(editor, x0-1, branch_height, z0+2, Block(wood))
    branch_height = randint(height, height+2)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0+4,branch_height+1,z0+4])
        place_block(editor, x0+4, branch_height+1, z0+4, Block(wood))
        place_block(editor, x0+3, branch_height, z0+3, Block(wood))
        place_block(editor, x0+2, branch_height, z0+2, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+4,branch_height+1,z0+3])
        place_block(editor, x0+4, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0+3, branch_height, z0+2, Block(wood))
        place_block(editor, x0+2, branch_height, z0+1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+5,branch_height+1,z0+3])
        place_block(editor, x0+5, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0+4, branch_height, z0+2, Block(wood))
        place_block(editor, x0+3, branch_height, z0+2, Block(wood))
        place_block(editor, x0+2, branch_height, z0+1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+3,branch_height+1,z0+4])
        place_block(editor, x0+3, branch_height+1, z0+4, Block(wood))
        place_block(editor, x0+2, branch_height, z0+3, Block(wood))
        place_block(editor, x0+1, branch_height, z0+2, Block(wood))
    elif branch_pos == 5:
        branches.append([x0+3,branch_height+1,z0+5])
        place_block(editor, x0+3, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0+2, branch_height, z0+4, Block(wood))
        place_block(editor, x0+2, branch_height, z0+3, Block(wood))
        place_block(editor, x0+1, branch_height, z0+2, Block(wood))

    branch_height = randint(height, height+2)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0-1,branch_height+1,z0-5])
        place_block(editor, x0-1, branch_height+1, z0-5, Block(wood))
        place_block(editor, x0-1, branch_height, z0-4, Block(wood))
        place_block(editor, x0, branch_height, z0-3, Block(wood))
        place_block(editor, x0, branch_height, z0-2, Block(wood))
    elif branch_pos == 2:
        branches.append([x0,branch_height+1,z0-5])
        place_block(editor, x0, branch_height+1, z0-5, Block(wood))
        place_block(editor, x0, branch_height, z0-4, Block(wood))
        place_block(editor, x0, branch_height, z0-3, Block(wood))
        place_block(editor, x0, branch_height, z0-2, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+1,branch_height+1,z0-5])
        place_block(editor, x0+1, branch_height+1, z0-5, Block(wood))
        place_block(editor, x0+1, branch_height, z0-4, Block(wood))
        place_block(editor, x0+1, branch_height, z0-3, Block(wood))
        place_block(editor, x0+1, branch_height, z0-2, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+2,branch_height+1,z0-5])
        place_block(editor, x0+2, branch_height+1, z0-5, Block(wood))
        place_block(editor, x0+2, branch_height, z0-4, Block(wood))
        place_block(editor, x0+1, branch_height, z0-3, Block(wood))
        place_block(editor, x0+1, branch_height, z0-2, Block(wood))
    elif branch_pos == 5:
        branches.append([x0-2,branch_height+1,z0-5])
        place_block(editor, x0-2, branch_height+1, z0-5, Block(wood))
        place_block(editor, x0-2, branch_height, z0-4, Block(wood))
        place_block(editor, x0-1, branch_height, z0-3, Block(wood))
        place_block(editor, x0-1, branch_height, z0-2, Block(wood))
    branch_height = randint(height, height+2)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0-1,branch_height+1,z0+5])
        place_block(editor, x0-1, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0-1, branch_height, z0+4, Block(wood))
        place_block(editor, x0, branch_height, z0+3, Block(wood))
        place_block(editor, x0, branch_height, z0+2, Block(wood))
    elif branch_pos == 2:
        branches.append([x0,branch_height+1,z0+5])
        place_block(editor, x0, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0, branch_height, z0+4, Block(wood))
        place_block(editor, x0, branch_height, z0+3, Block(wood))
        place_block(editor, x0, branch_height, z0+2, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+1,branch_height+1,z0+5])
        place_block(editor, x0+1, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0+1, branch_height, z0+4, Block(wood))
        place_block(editor, x0+1, branch_height, z0+3, Block(wood))
        place_block(editor, x0+1, branch_height, z0+2, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+2,branch_height+1,z0+5])
        place_block(editor, x0+2, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0+2, branch_height, z0+4, Block(wood))
        place_block(editor, x0+1, branch_height, z0+3, Block(wood))
        place_block(editor, x0+1, branch_height, z0+2, Block(wood))
    elif branch_pos == 5:
        branches.append([x0-2,branch_height+1,z0+5])
        place_block(editor, x0-2, branch_height+1, z0+5, Block(wood))
        place_block(editor, x0-2, branch_height, z0+4, Block(wood))
        place_block(editor, x0-1, branch_height, z0+3, Block(wood))
        place_block(editor, x0-1, branch_height, z0+2, Block(wood))
    branch_height = randint(height, height+2)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0-5,branch_height+1,z0-1])
        place_block(editor, x0-5, branch_height+1, z0-1, Block(wood))
        place_block(editor, x0-4, branch_height, z0-1, Block(wood))
        place_block(editor, x0-3, branch_height, z0, Block(wood))
        place_block(editor, x0-2, branch_height, z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-5,branch_height+1,z0])
        place_block(editor, x0-5, branch_height+1, z0, Block(wood))
        place_block(editor, x0-4, branch_height, z0, Block(wood))
        place_block(editor, x0-3, branch_height, z0, Block(wood))
        place_block(editor, x0-2, branch_height, z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-5,branch_height+1,z0+1])
        place_block(editor, x0-5, branch_height+1, z0+1, Block(wood))
        place_block(editor, x0-4, branch_height, z0+1, Block(wood))
        place_block(editor, x0-3, branch_height, z0+1, Block(wood))
        place_block(editor, x0-2, branch_height, z0+1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0-5,branch_height+1,z0+2])
        place_block(editor, x0-5, branch_height+1, z0+2, Block(wood))
        place_block(editor, x0-4, branch_height, z0+2, Block(wood))
        place_block(editor, x0-3, branch_height, z0+1, Block(wood))
        place_block(editor, x0-2, branch_height, z0+1, Block(wood))
    elif branch_pos == 5:
        branches.append([x0-5,branch_height+1,z0-2])
        place_block(editor, x0-5, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0-4, branch_height, z0-2, Block(wood))
        place_block(editor, x0-3, branch_height, z0-1, Block(wood))
        place_block(editor, x0-2, branch_height, z0-1, Block(wood))
    branch_height = randint(height, height+2)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0+5,branch_height+1,z0-1])
        place_block(editor, x0+5, branch_height+1, z0-1, Block(wood))
        place_block(editor, x0+4, branch_height, z0-1, Block(wood))
        place_block(editor, x0+3, branch_height, z0, Block(wood))
        place_block(editor, x0+2, branch_height, z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+5,branch_height+1,z0])
        place_block(editor, x0+5, branch_height+1, z0, Block(wood))
        place_block(editor, x0+4, branch_height, z0, Block(wood))
        place_block(editor, x0+3, branch_height, z0, Block(wood))
        place_block(editor, x0+2, branch_height, z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+5,branch_height+1,z0+1])
        place_block(editor, x0+5, branch_height+1, z0+1, Block(wood))
        place_block(editor, x0+4, branch_height, z0+1, Block(wood))
        place_block(editor, x0+3, branch_height, z0+1, Block(wood))
        place_block(editor, x0+2, branch_height, z0+1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+5,branch_height+1,z0+2])
        place_block(editor, x0+5, branch_height+1, z0+2, Block(wood))
        place_block(editor, x0+4, branch_height, z0+2, Block(wood))
        place_block(editor, x0+3, branch_height, z0+1, Block(wood))
        place_block(editor, x0+2, branch_height, z0+1, Block(wood))
    elif branch_pos == 5:
        branches.append([x0+5,branch_height+1,z0-2])
        place_block(editor, x0+5, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0+4, branch_height, z0-2, Block(wood))
        place_block(editor, x0+3, branch_height, z0-1, Block(wood))
        place_block(editor, x0+2, branch_height, z0-1, Block(wood))

    for branch in branches:
        x1, y1, z1 = branch[0], branch[1], branch[2]

        place_block(editor, x1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-2, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+3, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-3, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+3, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-3, Block(leaf), leaf_chance)
        place_block(editor, x1+3, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-3, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1+3, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-3, Block(leaf), leaf_chance)
        place_block(editor, x1+3, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-3, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+3, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-3, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1-2, Block(leaf), leaf_chance)

def generate_small_oak(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    stem_height = randint(4,7)
    for y in range (y0,stem_height+y0+2):
        if y == stem_height+y0+1:
            place_block(editor, x0, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
            continue
        place_block(editor, x0, y, z0, Block(wood))
        if y == int(stem_height/2 +y0)-1:
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
        elif y == stem_height+y0 or y == int(stem_height/2 +y0):
            place_block(editor, x0+2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)
        elif y>int(stem_height/2 +y0) and y<stem_height+y0:
            place_block(editor, x0+2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+2, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-2, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+2, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-2, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0-1, Block(leaf), leaf_chance)
            place_block(editor, x0+1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0-1, y, z0, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0+1, Block(leaf), leaf_chance)
            place_block(editor, x0, y, z0-1, Block(leaf), leaf_chance)

def generate_medium_oak(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(10,15)+y0
    branch_num = randint(3,7)
    branches = []
    branches.append([x0, height-1, z0])
    for y in range (y0,height): #tree stem
        place_block(editor, x0, y, z0, Block(wood))
        if y == y0:
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0+1, y, z0, Block(wood))
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0-1, y, z0, Block(wood))
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0, y, z0+1, Block(wood))
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0, y, z0-1, Block(wood))

    
    for a in range (0, branch_num):
        branch_height = randint(int((height-y0)/2+y0)+4, height-1)
        branch_pos = randint(1, 24)
        if branch_pos == 1:
            branches.append([x0+3,branch_height,z0])
            place_block(editor, x0+3, branch_height, z0, Block(wood))
            place_block(editor, x0+2, branch_height-1, z0, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0, Block(wood))
        elif branch_pos == 2:
            branches.append([x0+3,branch_height,z0+1])
            place_block(editor, x0+3,branch_height,z0+1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+2,branch_height-1,z0+1, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-1,z0, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0, Block(wood))
        elif branch_pos == 3:
            branches.append([x0+3,branch_height,z0+2])
            place_block(editor, x0+3,branch_height,z0+2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+2,branch_height-1,z0+1, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 4:
            branches.append([x0+3,branch_height,z0+3])
            place_block(editor, x0+3, branch_height, z0+3, Block(wood))
            place_block(editor, x0+2, branch_height-1, z0+2, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0+1, Block(wood))  
        elif branch_pos == 5:
            branches.append([x0+2,branch_height,z0+3])
            place_block(editor, x0+2,branch_height,z0+3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+2,branch_height-1,z0+2, Block(wood))
            else:
                place_block(editor, x0+1,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 6:
            branches.append([x0+1,branch_height,z0+3])
            place_block(editor, x0+1,branch_height,z0+3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-1,z0+2, Block(wood))
            else:
                place_block(editor, x0,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 7:
            branches.append([x0,branch_height,z0+3])
            place_block(editor, x0, branch_height, z0+3, Block(wood))
            place_block(editor, x0, branch_height-1, z0+2, Block(wood))
            place_block(editor, x0, branch_height-1, z0+1, Block(wood))
        elif branch_pos == 8:
            branches.append([x0-1,branch_height,z0+3])
            place_block(editor, x0-1,branch_height,z0+3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-1,z0+2, Block(wood))
            else:
                place_block(editor, x0,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 9:
            branches.append([x0-2,branch_height,z0+3])
            place_block(editor, x0-2,branch_height,z0+3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-2,branch_height-1,z0+2, Block(wood))
            else:
                place_block(editor, x0-1,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 10:
            branches.append([x0-3,branch_height,z0+3])
            place_block(editor, x0-3, branch_height, z0+3, Block(wood))
            place_block(editor, x0-2, branch_height-1, z0+2, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0+1, Block(wood)) 
        elif branch_pos == 11:
            branches.append([x0-3,branch_height,z0+2])
            place_block(editor, x0-3,branch_height,z0+2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-2,branch_height-1,z0+1, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 12:
            branches.append([x0-3,branch_height,z0+1])
            place_block(editor, x0-3,branch_height,z0+1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-2,branch_height-1,z0+1, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-1,z0, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0, Block(wood))
        elif branch_pos == 13:
            branches.append([x0-3,branch_height,z0])
            place_block(editor, x0-3, branch_height, z0, Block(wood))
            place_block(editor, x0-2, branch_height-1, z0, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0, Block(wood))
        elif branch_pos == 14:
            branches.append([x0-3,branch_height,z0-1])
            place_block(editor, x0-3,branch_height,z0-1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-2,branch_height-1,z0-1, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-1,z0, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0, Block(wood))
        elif branch_pos == 15:
            branches.append([x0-3,branch_height,z0-2])
            place_block(editor, x0-3,branch_height,z0-2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-2,branch_height-1,z0-1, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 16:
            branches.append([x0-3,branch_height,z0-3])
            place_block(editor, x0-3, branch_height, z0-3, Block(wood))
            place_block(editor, x0-2, branch_height-1, z0-2, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0-1, Block(wood)) 
        elif branch_pos == 17:
            branches.append([x0-2,branch_height,z0-3])
            place_block(editor, x0-2,branch_height,z0-3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-2,branch_height-1,z0-2, Block(wood))
            else:
                place_block(editor, x0-1,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 18:
            branches.append([x0-1,branch_height,z0-3])
            place_block(editor, x0-1,branch_height,z0-3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-1,z0-2, Block(wood))
            else:
                place_block(editor, x0,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 19:
            branches.append([x0,branch_height,z0-3])
            place_block(editor, x0, branch_height, z0-3, Block(wood))
            place_block(editor, x0, branch_height-1, z0-2, Block(wood))
            place_block(editor, x0, branch_height-1, z0-1, Block(wood))
        elif branch_pos == 20:
            branches.append([x0+1,branch_height,z0-3])
            place_block(editor, x0+1,branch_height,z0-3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-1,z0-2, Block(wood))
            else:
                place_block(editor, x0,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 21:
            branches.append([x0+2,branch_height,z0-3])
            place_block(editor, x0+2,branch_height,z0-3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+2,branch_height-1,z0-2, Block(wood))
            else:
                place_block(editor, x0+1,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 22:
            branches.append([x0+3,branch_height,z0-3])
            place_block(editor, x0+3, branch_height, z0-3, Block(wood))
            place_block(editor, x0+2, branch_height-1, z0-2, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0-1, Block(wood))
        elif branch_pos == 23:
            branches.append([x0+3,branch_height,z0-2])
            place_block(editor, x0+3,branch_height,z0-2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+2,branch_height-1,z0-1, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 24:
            branches.append([x0+3,branch_height,z0-1])
            place_block(editor, x0+3,branch_height,z0-1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+2,branch_height-1,z0-1, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-1,z0, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0, Block(wood))
        


    for branch in branches:
        x1, y1, z1 = branch[0], branch[1], branch[2]

        place_block(editor, x1+1, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1, Block(leaf), leaf_chance)

        place_block(editor, x1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1-2, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-1, Block(leaf), leaf_chance)

def generate_large_oak(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(16,23)+y0
    branch_num = randint(5,10)
    branches = []
    branches.append([x0, height-1, z0])
    for y in range (y0,height): #tree stem
        place_block(editor, x0, y, z0, Block(wood))
        if y == y0:
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0+1, y, z0, Block(wood))
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0-1, y, z0, Block(wood))
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0, y, z0+1, Block(wood))
            chance = randint(1,4)
            if chance != 4:
                place_block(editor, x0, y, z0-1, Block(wood))

    
    for a in range (0, branch_num):
        branch_height = randint(int((height-y0)/2+y0)+5, height-1)
        branch_pos = randint(1, 40)
        if branch_pos == 1:
            branches.append([x0+5,branch_height,z0])
            place_block(editor, x0+5, branch_height, z0, Block(wood))
            place_block(editor, x0+4, branch_height-1, z0, Block(wood))
            place_block(editor, x0+3, branch_height-2, z0, Block(wood))
            place_block(editor, x0+2, branch_height-2, z0, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0, Block(wood))
        elif branch_pos == 2:
            branches.append([x0+5,branch_height,z0+1])
            place_block(editor, x0+5,branch_height,z0+1, Block(wood))
            place_block(editor, x0+4, branch_height-1, z0+1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+3,branch_height-2,z0+1, Block(wood))
            else:
                place_block(editor, x0+3,branch_height-2,z0, Block(wood))
            place_block(editor, x0+2, branch_height-2, z0, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0, Block(wood))
        elif branch_pos == 3:
            branches.append([x0+5,branch_height,z0+2])
            place_block(editor, x0+5, branch_height, z0+2, Block(wood))
            place_block(editor, x0+4, branch_height-1, z0+2, Block(wood))
            place_block(editor, x0+3, branch_height-2, z0+1, Block(wood))
            place_block(editor, x0+2, branch_height-2, z0+1, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0, Block(wood))
        elif branch_pos == 4:
            branches.append([x0+5,branch_height,z0+3])
            place_block(editor, x0+5, branch_height, z0+3, Block(wood))
            place_block(editor, x0+4, branch_height-1, z0+3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+3,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0+2, Block(wood))
            elif b==2:
                place_block(editor, x0+3,branch_height-2,z0+2, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0+2, Block(wood))
            else:
                place_block(editor, x0+3,branch_height-2,z0+2, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0+1, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0+1, Block(wood)) 
        elif branch_pos == 5:
            branches.append([x0+5,branch_height,z0+4])
            place_block(editor, x0+5, branch_height, z0+4, Block(wood))
            place_block(editor, x0+4, branch_height-1, z0+3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+3,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0+2, Block(wood))
            elif b==2:
                place_block(editor, x0+3,branch_height-2,z0+2, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0+2, Block(wood))
            else:
                place_block(editor, x0+3,branch_height-2,z0+2, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0+1, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0+1, Block(wood)) 
        elif branch_pos == 6:
            branches.append([x0+5,branch_height,z0+5])
            place_block(editor, x0+5, branch_height, z0+5, Block(wood))
            place_block(editor, x0+4, branch_height-1, z0+4, Block(wood))
            place_block(editor, x0+3, branch_height-2, z0+3, Block(wood))
            place_block(editor, x0+2, branch_height-2, z0+2, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0+1, Block(wood))
        elif branch_pos == 7:
            branches.append([x0+4,branch_height,z0+5])
            place_block(editor, x0+4, branch_height, z0+5, Block(wood))
            place_block(editor, x0+3, branch_height-1, z0+4, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+3,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0+2, Block(wood))
            elif b==2:
                place_block(editor, x0+2,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0+2, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0+1, branch_height-2, z0+2, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0+1, Block(wood)) 
        elif branch_pos == 8:
            branches.append([x0+3,branch_height,z0+5])
            place_block(editor, x0+3, branch_height, z0+5, Block(wood))
            place_block(editor, x0+3, branch_height-1, z0+4, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+3,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0+2, Block(wood))
            elif b==2:
                place_block(editor, x0+2,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0+2, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0+1, branch_height-2, z0+2, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0+1, Block(wood)) 
        elif branch_pos == 9:
            branches.append([x0+2,branch_height,z0+5])
            place_block(editor, x0+2, branch_height, z0+5, Block(wood))
            place_block(editor, x0+2, branch_height-1, z0+4, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0+3, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0+2, Block(wood))
            place_block(editor, x0, branch_height-2, z0+1, Block(wood))
        elif branch_pos == 10:
            branches.append([x0+1,branch_height,z0+5])
            place_block(editor, x0+1,branch_height,z0+5, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0+4, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-2,z0+3, Block(wood))
            else:
                place_block(editor, x0,branch_height-2,z0+3, Block(wood))
            place_block(editor, x0, branch_height-2, z0+2, Block(wood))
            place_block(editor, x0, branch_height-2, z0+1, Block(wood))
        if branch_pos == 11:
            branches.append([x0,branch_height,z0+5])
            place_block(editor, x0, branch_height, z0+5, Block(wood))
            place_block(editor, x0, branch_height-1, z0+4, Block(wood))
            place_block(editor, x0, branch_height-2, z0+3, Block(wood))
            place_block(editor, x0, branch_height-2, z0+2, Block(wood))
            place_block(editor, x0, branch_height-2, z0+1, Block(wood))
        elif branch_pos == 12:
            branches.append([x0-1,branch_height,z0+5])
            place_block(editor, x0-1,branch_height,z0+5, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0+4, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-2,z0+3, Block(wood))
            else:
                place_block(editor, x0,branch_height-2,z0+3, Block(wood))
            place_block(editor, x0, branch_height-2, z0+2, Block(wood))
            place_block(editor, x0, branch_height-2, z0+1, Block(wood))
        elif branch_pos == 13:
            branches.append([x0-2,branch_height,z0+5])
            place_block(editor, x0-2, branch_height, z0+5, Block(wood))
            place_block(editor, x0-2, branch_height-1, z0+4, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0+3, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0+2, Block(wood))
            place_block(editor, x0, branch_height-2, z0+1, Block(wood))
        elif branch_pos == 14:
            branches.append([x0-3,branch_height,z0+5])
            place_block(editor, x0-3, branch_height, z0+5, Block(wood))
            place_block(editor, x0-3, branch_height-1, z0+4, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-3,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0+2, Block(wood))
            elif b==2:
                place_block(editor, x0-2,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0+2, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0-1, branch_height-2, z0+2, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0+1, Block(wood)) 
        elif branch_pos == 15:
            branches.append([x0-4,branch_height,z0+5])
            place_block(editor, x0-4, branch_height, z0+5, Block(wood))
            place_block(editor, x0-3, branch_height-1, z0+4, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-3,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0+2, Block(wood))
            elif b==2:
                place_block(editor, x0-2,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0+2, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0-1, branch_height-2, z0+2, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0+1, Block(wood)) 
        elif branch_pos == 16:
            branches.append([x0-5,branch_height,z0+5])
            place_block(editor, x0-5, branch_height, z0+5, Block(wood))
            place_block(editor, x0-4, branch_height-1, z0+4, Block(wood))
            place_block(editor, x0-3, branch_height-2, z0+3, Block(wood))
            place_block(editor, x0-2, branch_height-2, z0+2, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0+1, Block(wood))
        elif branch_pos == 17:
            branches.append([x0-5,branch_height,z0+4])
            place_block(editor, x0-5, branch_height, z0+4, Block(wood))
            place_block(editor, x0-4, branch_height-1, z0+3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-3,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0+2, Block(wood))
            elif b==2:
                place_block(editor, x0-3,branch_height-2,z0+2, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0+2, Block(wood))
            else:
                place_block(editor, x0-3,branch_height-2,z0+2, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0+1, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0+1, Block(wood)) 
        elif branch_pos == 18:
            branches.append([x0-5,branch_height,z0+3])
            place_block(editor, x0-5, branch_height, z0+3, Block(wood))
            place_block(editor, x0-4, branch_height-1, z0+3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-3,branch_height-2,z0+3, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0+2, Block(wood))
            elif b==2:
                place_block(editor, x0-3,branch_height-2,z0+2, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0+2, Block(wood))
            else:
                place_block(editor, x0-3,branch_height-2,z0+2, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0+1, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0+1, Block(wood)) 
        elif branch_pos == 19:
            branches.append([x0-5,branch_height,z0+2])
            place_block(editor, x0-5, branch_height, z0+2, Block(wood))
            place_block(editor, x0-4, branch_height-1, z0+2, Block(wood))
            place_block(editor, x0-3, branch_height-2, z0+1, Block(wood))
            place_block(editor, x0-2, branch_height-2, z0+1, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0, Block(wood))
        elif branch_pos == 20:
            branches.append([x0-5,branch_height,z0+1])
            place_block(editor, x0-5,branch_height,z0+1, Block(wood))
            place_block(editor, x0-4, branch_height-1, z0+1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-3,branch_height-2,z0+1, Block(wood))
            else:
                place_block(editor, x0-3,branch_height-2,z0, Block(wood))
            place_block(editor, x0-2, branch_height-2, z0, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0, Block(wood))
        if branch_pos == 21:
            branches.append([x0-5,branch_height,z0])
            place_block(editor, x0-5, branch_height, z0, Block(wood))
            place_block(editor, x0-4, branch_height-1, z0, Block(wood))
            place_block(editor, x0-3, branch_height-2, z0, Block(wood))
            place_block(editor, x0-2, branch_height-2, z0, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0, Block(wood))
        elif branch_pos == 22:
            branches.append([x0-5,branch_height,z0-1])
            place_block(editor, x0-5,branch_height,z0-1, Block(wood))
            place_block(editor, x0-4, branch_height-1, z0-1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-3,branch_height-2,z0-1, Block(wood))
            else:
                place_block(editor, x0-3,branch_height-2,z0, Block(wood))
            place_block(editor, x0-2, branch_height-2, z0, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0, Block(wood))
        elif branch_pos == 23:
            branches.append([x0-5,branch_height,z0-2])
            place_block(editor, x0-5, branch_height, z0-2, Block(wood))
            place_block(editor, x0-4, branch_height-1, z0-2, Block(wood))
            place_block(editor, x0-3, branch_height-2, z0-1, Block(wood))
            place_block(editor, x0-2, branch_height-2, z0-1, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0, Block(wood))
        elif branch_pos == 24:
            branches.append([x0-5,branch_height,z0-3])
            place_block(editor, x0-5, branch_height, z0-3, Block(wood))
            place_block(editor, x0-4, branch_height-1, z0-3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-3,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0-2, Block(wood))
            elif b==2:
                place_block(editor, x0-3,branch_height-2,z0-2, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0-2, Block(wood))
            else:
                place_block(editor, x0-3,branch_height-2,z0-2, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0-1, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0-1, Block(wood))
        elif branch_pos == 25:
            branches.append([x0-5,branch_height,z0-4])
            place_block(editor, x0-5, branch_height, z0-4, Block(wood))
            place_block(editor, x0-4, branch_height-1, z0-3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-3,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0-2, Block(wood))
            elif b==2:
                place_block(editor, x0-3,branch_height-2,z0-2, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0-2, Block(wood))
            else:
                place_block(editor, x0-3,branch_height-2,z0-2, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0-1, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0-1, Block(wood)) 
        elif branch_pos == 26:
            branches.append([x0-5,branch_height,z0-5])
            place_block(editor, x0-5, branch_height, z0-5, Block(wood))
            place_block(editor, x0-4, branch_height-1, z0-4, Block(wood))
            place_block(editor, x0-3, branch_height-2, z0-3, Block(wood))
            place_block(editor, x0-2, branch_height-2, z0-2, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0-1, Block(wood))
        elif branch_pos == 27:
            branches.append([x0+5,branch_height,z0-5])
            place_block(editor, x0+5, branch_height, z0-5, Block(wood))
            place_block(editor, x0+4, branch_height-1, z0-4, Block(wood))
            place_block(editor, x0+3, branch_height-2, z0-3, Block(wood))
            place_block(editor, x0+2, branch_height-2, z0-2, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0-1, Block(wood))
        elif branch_pos == 28:
            branches.append([x0+4,branch_height,z0-5])
            place_block(editor, x0+4, branch_height, z0-5, Block(wood))
            place_block(editor, x0+3, branch_height-1, z0-4, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+3,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0-2, Block(wood))
            elif b==2:
                place_block(editor, x0+2,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0-2, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0+1, branch_height-2, z0-2, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0-1, Block(wood)) 
        elif branch_pos == 29:
            branches.append([x0+3,branch_height,z0-5])
            place_block(editor, x0+3, branch_height, z0-5, Block(wood))
            place_block(editor, x0+3, branch_height-1, z0-4, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+3,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0-2, Block(wood))
            elif b==2:
                place_block(editor, x0+2,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0-2, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0+1, branch_height-2, z0-2, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0-1, Block(wood)) 
        elif branch_pos == 30:
            branches.append([x0+2,branch_height,z0-5])
            place_block(editor, x0+2, branch_height, z0-5, Block(wood))
            place_block(editor, x0+2, branch_height-1, z0-4, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0-3, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0-2, Block(wood))
            place_block(editor, x0, branch_height-2, z0-1, Block(wood))
        elif branch_pos == 31:
            branches.append([x0+1,branch_height,z0-5])
            place_block(editor, x0+1,branch_height,z0-5, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0-4, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-2,z0-3, Block(wood))
            else:
                place_block(editor, x0,branch_height-2,z0-3, Block(wood))
            place_block(editor, x0, branch_height-2, z0-2, Block(wood))
            place_block(editor, x0, branch_height-2, z0-1, Block(wood))
        elif branch_pos == 32:
            branches.append([x0,branch_height,z0-5])
            place_block(editor, x0, branch_height, z0-5, Block(wood))
            place_block(editor, x0, branch_height-1, z0-4, Block(wood))
            place_block(editor, x0, branch_height-2, z0-3, Block(wood))
            place_block(editor, x0, branch_height-2, z0-2, Block(wood))
            place_block(editor, x0, branch_height-2, z0-1, Block(wood))
        elif branch_pos == 33:
            branches.append([x0-1,branch_height,z0-5])
            place_block(editor, x0-1,branch_height,z0-5, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0-4, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-2,z0-3, Block(wood))
            else:
                place_block(editor, x0,branch_height-2,z0-3, Block(wood))
            place_block(editor, x0, branch_height-2, z0-2, Block(wood))
            place_block(editor, x0, branch_height-2, z0-1, Block(wood))
        elif branch_pos == 34:
            branches.append([x0-2,branch_height,z0-5])
            place_block(editor, x0-2, branch_height, z0-5, Block(wood))
            place_block(editor, x0-2, branch_height-1, z0-4, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0-3, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0-2, Block(wood))
            place_block(editor, x0, branch_height-2, z0-1, Block(wood))
        elif branch_pos == 35:
            branches.append([x0-3,branch_height,z0-5])
            place_block(editor, x0-3, branch_height, z0-5, Block(wood))
            place_block(editor, x0-3, branch_height-1, z0-4, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-3,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0-2, Block(wood))
            elif b==2:
                place_block(editor, x0-2,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0-2, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0-1, branch_height-2, z0-2, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0-1, Block(wood)) 
        elif branch_pos == 36:
            branches.append([x0-4,branch_height,z0-5])
            place_block(editor, x0-4, branch_height, z0-5, Block(wood))
            place_block(editor, x0-3, branch_height-1, z0-4, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0-3,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0-2, Block(wood))
            elif b==2:
                place_block(editor, x0-2,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0-2, branch_height-2, z0-2, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0-1, branch_height-2, z0-2, Block(wood))
            place_block(editor, x0-1, branch_height-2, z0-1, Block(wood))
        elif branch_pos == 37:
            branches.append([x0+5,branch_height,z0-1])
            place_block(editor, x0+5,branch_height,z0-1, Block(wood))
            place_block(editor, x0+4, branch_height-1, z0-1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+3,branch_height-2,z0-1, Block(wood))
            else:
                place_block(editor, x0+3,branch_height-2,z0, Block(wood))
            place_block(editor, x0+2, branch_height-2, z0, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0, Block(wood))
        elif branch_pos == 38:
            branches.append([x0+5,branch_height,z0-2])
            place_block(editor, x0+5, branch_height, z0-2, Block(wood))
            place_block(editor, x0+4, branch_height-1, z0-2, Block(wood))
            place_block(editor, x0+3, branch_height-2, z0-1, Block(wood))
            place_block(editor, x0+2, branch_height-2, z0-1, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0, Block(wood))
        elif branch_pos == 39:
            branches.append([x0+5,branch_height,z0-3])
            place_block(editor, x0+5, branch_height, z0-3, Block(wood))
            place_block(editor, x0+4, branch_height-1, z0-3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+3,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0-2, Block(wood))
            elif b==2:
                place_block(editor, x0+3,branch_height-2,z0-2, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0-2, Block(wood))
            else:
                place_block(editor, x0+3,branch_height-2,z0-2, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0-1, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0-1, Block(wood)) 
        elif branch_pos == 40:
            branches.append([x0+5,branch_height,z0-4])
            place_block(editor, x0+5, branch_height, z0-4, Block(wood))
            place_block(editor, x0+4, branch_height-1, z0-3, Block(wood))
            b = randint(1,3)
            if b==1:
                place_block(editor, x0+3,branch_height-2,z0-3, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0-2, Block(wood))
            elif b==2:
                place_block(editor, x0+3,branch_height-2,z0-2, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0-2, Block(wood))
            else:
                place_block(editor, x0+3,branch_height-2,z0-2, Block(wood))
                place_block(editor, x0+2, branch_height-2, z0-1, Block(wood))
            place_block(editor, x0+1, branch_height-2, z0-1, Block(wood)) 
            


    for branch in branches:
        x1, y1, z1 = branch[0], branch[1], branch[2]
        if x1 == x0 and z1 == z0:
            #more leaves for the main stem/branch
            place_block(editor, x1+1, y1+3, z1+1, Block(leaf), leaf_chance)
            place_block(editor, x1-1, y1+3, z1-1, Block(leaf), leaf_chance)
            place_block(editor, x1-1, y1+3, z1+1, Block(leaf), leaf_chance)
            place_block(editor, x1+1, y1+3, z1-1, Block(leaf), leaf_chance)

            place_block(editor, x1+3, y1+2, z1, Block(leaf), leaf_chance)
            place_block(editor, x1-3, y1+2, z1, Block(leaf), leaf_chance)
            place_block(editor, x1, y1+2, z1+3, Block(leaf), leaf_chance)
            place_block(editor, x1, y1+2, z1-3, Block(leaf), leaf_chance)
            place_block(editor, x1+2, y1+2, z1+2, Block(leaf), leaf_chance)
            place_block(editor, x1-2, y1+2, z1-2, Block(leaf), leaf_chance)
            place_block(editor, x1-2, y1+2, z1+2, Block(leaf), leaf_chance)
            place_block(editor, x1+2, y1+2, z1-2, Block(leaf), leaf_chance)

            place_block(editor, x1+4, y1+1, z1+1, Block(leaf), leaf_chance)
            place_block(editor, x1-4, y1+1, z1-1, Block(leaf), leaf_chance)
            place_block(editor, x1-4, y1+1, z1+1, Block(leaf), leaf_chance)
            place_block(editor, x1+4, y1+1, z1-1, Block(leaf), leaf_chance)
            place_block(editor, x1+1, y1+1, z1+4, Block(leaf), leaf_chance)
            place_block(editor, x1-1, y1+1, z1+4, Block(leaf), leaf_chance)
            place_block(editor, x1+1, y1+1, z1-4, Block(leaf), leaf_chance)
            place_block(editor, x1-1, y1+1, z1-4, Block(leaf), leaf_chance)
            place_block(editor, x1+4, y1+1, z1, Block(leaf), leaf_chance)
            place_block(editor, x1-4, y1+1, z1, Block(leaf), leaf_chance)
            place_block(editor, x1, y1+1, z1+4, Block(leaf), leaf_chance)
            place_block(editor, x1, y1+1, z1-4, Block(leaf), leaf_chance)
            place_block(editor, x1+3, y1+1, z1+3, Block(leaf), leaf_chance)
            place_block(editor, x1-3, y1+1, z1-3, Block(leaf), leaf_chance)
            place_block(editor, x1-3, y1+1, z1+3, Block(leaf), leaf_chance)
            place_block(editor, x1+3, y1+1, z1-3, Block(leaf), leaf_chance)
            place_block(editor, x1+2, y1+1, z1+3, Block(leaf), leaf_chance)
            place_block(editor, x1-2, y1+1, z1+3, Block(leaf), leaf_chance)
            place_block(editor, x1+2, y1+1, z1-3, Block(leaf), leaf_chance)
            place_block(editor, x1-2, y1+1, z1-3, Block(leaf), leaf_chance)
            place_block(editor, x1+3, y1+1, z1+2, Block(leaf), leaf_chance)
            place_block(editor, x1-3, y1+1, z1-2, Block(leaf), leaf_chance)
            place_block(editor, x1-3, y1+1, z1+2, Block(leaf), leaf_chance)
            place_block(editor, x1+3, y1+1, z1-2, Block(leaf), leaf_chance)

            place_block(editor, x1+2, y1, z1-1, Block(leaf), leaf_chance)
            place_block(editor, x1-2, y1, z1-1, Block(leaf), leaf_chance)
            place_block(editor, x1-1, y1, z1+2, Block(leaf), leaf_chance)
            place_block(editor, x1-1, y1, z1-2, Block(leaf), leaf_chance)
            place_block(editor, x1+2, y1, z1+1, Block(leaf), leaf_chance)
            place_block(editor, x1-2, y1, z1+1, Block(leaf), leaf_chance)
            place_block(editor, x1+1, y1, z1+2, Block(leaf), leaf_chance)
            place_block(editor, x1+1, y1, z1-2, Block(leaf), leaf_chance)

        else:
            place_block(editor, x1, y1-1, z1, Block(leaf), leaf_chance)
        
        place_block(editor, x1+1, y1+3, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+3, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+3, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+3, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+3, z1, Block(leaf), leaf_chance)

        place_block(editor, x1, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+2, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+2, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+2, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+2, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+2, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+2, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+2, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+2, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+2, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+2, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+2, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+2, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+2, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+2, z1-2, Block(leaf), leaf_chance)

        place_block(editor, x1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+3, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-3, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-3, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+3, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1+3, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1+3, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1-3, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1-3, Block(leaf), leaf_chance)
        place_block(editor, x1+3, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-3, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+3, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-3, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-2, Block(leaf), leaf_chance)
        
def generate_mega_oak(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    generate_large_oak(point, editor, wood, leaf, leaf_chance)
    x0, y0, z0 = point.x, point.y, point.z
    new_point = ivec3(x0+1, y0, z0)
    generate_large_oak(new_point, editor, wood, leaf, leaf_chance)
    new_point = ivec3(x0+1, y0, z0+1)
    generate_large_oak(new_point, editor, wood, leaf, leaf_chance)
    new_point = ivec3(x0, y0, z0+1)
    generate_large_oak(new_point, editor, wood, leaf, leaf_chance)

def generate_small_jungle(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(7,12)+y0
    branches = []
    
    for y in range (y0,height+1): #tree stem
        place_block(editor, x0, y, z0, Block(wood))

    branches.append([x0, height, z0])

    # random branch generation, 1 random branch for each quadrant
    branch_height = randint(height-4, height-2)
    branch_pos = randint(1, 4)
    if branch_pos == 1:
        branches.append([x0-2,branch_height+1,z0])
        place_block(editor, x0-2, branch_height+1, z0, Block(wood))
        place_block(editor, x0-1, branch_height, z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-2,branch_height+1,z0-1])
        place_block(editor, x0-2, branch_height+1, z0-1, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0-1,branch_height,z0-1, Block(wood))
        else:
            place_block(editor, x0-1,branch_height,z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-2,branch_height+1,z0-2])
        place_block(editor, x0-2, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0-1,branch_height,z0-1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0-1,branch_height+1,z0-2])
        place_block(editor, x0-1, branch_height+1, z0-2, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0-1,branch_height,z0-1, Block(wood))
        else:
            place_block(editor, x0,branch_height,z0-1, Block(wood))
    branch_height = randint(height-4, height-2)
    branch_pos = randint(1, 4)
    if branch_pos == 1:
        branches.append([x0,branch_height+1,z0-2])
        place_block(editor, x0, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0, branch_height, z0-1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+2,branch_height+1,z0-1])
        place_block(editor, x0+2, branch_height+1, z0-1, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0+1,branch_height,z0-1, Block(wood))
        else:
            place_block(editor, x0+1,branch_height,z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+2,branch_height+1,z0-2])
        place_block(editor, x0+2, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0+1,branch_height,z0-1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+1,branch_height+1,z0-2])
        place_block(editor, x0+1, branch_height+1, z0-2, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0+1,branch_height,z0-1, Block(wood))
        else:
            place_block(editor, x0,branch_height,z0-1, Block(wood))
    branch_height = randint(height-4, height-2)
    branch_pos = randint(1, 4)
    if branch_pos == 1:
        branches.append([x0+2,branch_height+1,z0])
        place_block(editor, x0+2, branch_height+1, z0, Block(wood))
        place_block(editor, x0+1, branch_height, z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+2,branch_height+1,z0+1])
        place_block(editor, x0+2, branch_height+1, z0+1, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0+1,branch_height,z0+1, Block(wood))
        else:
            place_block(editor, x0+1,branch_height,z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+2,branch_height+1,z0+2])
        place_block(editor, x0+2, branch_height+1, z0+2, Block(wood))
        place_block(editor, x0+1,branch_height,z0+1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+1,branch_height+1,z0+2])
        place_block(editor, x0+1, branch_height+1, z0+2, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0+1,branch_height,z0+1, Block(wood))
        else:
            place_block(editor, x0,branch_height,z0+1, Block(wood))
    branch_height = randint(height-4, height-2)
    branch_pos = randint(1, 4)
    if branch_pos == 1:
        branches.append([x0,branch_height+1,z0+2])
        place_block(editor, x0, branch_height+1, z0+2, Block(wood))
        place_block(editor, x0, branch_height, z0+1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-2,branch_height+1,z0+1])
        place_block(editor, x0-2, branch_height+1, z0+1, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0-1,branch_height,z0+1, Block(wood))
        else:
            place_block(editor, x0-1,branch_height,z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-2,branch_height+1,z0+2])
        place_block(editor, x0-2, branch_height+1, z0+2, Block(wood))
        place_block(editor, x0-1,branch_height,z0+1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0-1,branch_height+1,z0+2])
        place_block(editor, x0-1, branch_height+1, z0+2, Block(wood))
        b = randint(1,2)
        if b==1:
            place_block(editor, x0-1,branch_height,z0+1, Block(wood))
        else:
            place_block(editor, x0,branch_height,z0+1, Block(wood))

    for branch in branches:
        x1, y1, z1 = branch[0], branch[1], branch[2]

        place_block(editor, x1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-1, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-2, Block(leaf), leaf_chance)

def generate_medium_jungle(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(10,18)+y0
    branches = []
    
    for y in range (y0,height+1): #tree stem
        place_block(editor, x0, y, z0, Block(wood))

    branches.append([x0, height, z0])

    # random branch generation, 1 random branch for each quadrant
    branch_height = randint(height-5, height-2)
    branch_pos = randint(1, 3)
    if branch_pos == 1:
        branches.append([x0-3,branch_height+1,z0-3])
        place_block(editor, x0-3, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0-2, branch_height, z0-2, Block(wood))
        place_block(editor, x0-1, branch_height, z0-1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-2,branch_height+1,z0-3])
        place_block(editor, x0-2, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0-2, branch_height, z0-2, Block(wood))
        place_block(editor, x0-1, branch_height, z0-1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-3,branch_height+1,z0-2])
        place_block(editor, x0-3, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0-2, branch_height, z0-2, Block(wood))
        place_block(editor, x0-1, branch_height, z0-1, Block(wood))
    branch_height = randint(height-5, height-2)
    branch_pos = randint(1, 3)
    if branch_pos == 1:
        branches.append([x0-3,branch_height+1,z0+3])
        place_block(editor, x0-3, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0-2, branch_height, z0+2, Block(wood))
        place_block(editor, x0-1, branch_height, z0+1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-2,branch_height+1,z0+3])
        place_block(editor, x0-2, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0-2, branch_height, z0+2, Block(wood))
        place_block(editor, x0-1, branch_height, z0+1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-3,branch_height+1,z0+2])
        place_block(editor, x0-3, branch_height+1, z0+2, Block(wood))
        place_block(editor, x0-2, branch_height, z0+2, Block(wood))
        place_block(editor, x0-1, branch_height, z0+1, Block(wood))
    branch_height = randint(height-5, height-2)
    branch_pos = randint(1, 3)
    if branch_pos == 1:
        branches.append([x0+3,branch_height+1,z0+3])
        place_block(editor, x0+3, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0+2, branch_height, z0+2, Block(wood))
        place_block(editor, x0+1, branch_height, z0+1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+2,branch_height+1,z0+3])
        place_block(editor, x0+2, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0+2, branch_height, z0+2, Block(wood))
        place_block(editor, x0+1, branch_height, z0+1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+3,branch_height+1,z0+2])
        place_block(editor, x0+3, branch_height+1, z0+2, Block(wood))
        place_block(editor, x0+2, branch_height, z0+2, Block(wood))
        place_block(editor, x0+1, branch_height, z0+1, Block(wood))
    branch_height = randint(height-5, height-2)
    branch_pos = randint(1, 3)
    if branch_pos == 1:
        branches.append([x0+3,branch_height+1,z0-3])
        place_block(editor, x0+3, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0+2, branch_height, z0-2, Block(wood))
        place_block(editor, x0+1, branch_height, z0-1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+2,branch_height+1,z0-3])
        place_block(editor, x0+2, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0+2, branch_height, z0-2, Block(wood))
        place_block(editor, x0+1, branch_height, z0-1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+3,branch_height+1,z0-2])
        place_block(editor, x0+3, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0+2, branch_height, z0-2, Block(wood))
        place_block(editor, x0+1, branch_height, z0-1, Block(wood))
    branch_height = randint(height-5, height-2)
    branch_pos = randint(1, 3)
    if branch_pos == 1:
        branches.append([x0-3,branch_height+1,z0-1])
        place_block(editor, x0-3, branch_height+1, z0-1, Block(wood))
        place_block(editor, x0-2, branch_height, z0-1, Block(wood))
        place_block(editor, x0-1, branch_height, z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-3,branch_height+1,z0])
        place_block(editor, x0-3, branch_height+1, z0, Block(wood))
        place_block(editor, x0-2, branch_height, z0, Block(wood))
        place_block(editor, x0-1, branch_height, z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-3,branch_height+1,z0+1])
        place_block(editor, x0-3, branch_height+1, z0+1, Block(wood))
        place_block(editor, x0-2, branch_height, z0+1, Block(wood))
        place_block(editor, x0-1, branch_height, z0, Block(wood))
    branch_height = randint(height-5, height-2)
    branch_pos = randint(1, 3)
    if branch_pos == 1:
        branches.append([x0+3,branch_height+1,z0-1])
        place_block(editor, x0+3, branch_height+1, z0-1, Block(wood))
        place_block(editor, x0+2, branch_height, z0-1, Block(wood))
        place_block(editor, x0+1, branch_height, z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+3,branch_height+1,z0])
        place_block(editor, x0+3, branch_height+1, z0, Block(wood))
        place_block(editor, x0+2, branch_height, z0, Block(wood))
        place_block(editor, x0+1, branch_height, z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+3,branch_height+1,z0+1])
        place_block(editor, x0+3, branch_height+1, z0+1, Block(wood))
        place_block(editor, x0+2, branch_height, z0+1, Block(wood))
        place_block(editor, x0+1, branch_height, z0, Block(wood))
    branch_height = randint(height-5, height-2)
    branch_pos = randint(1, 3)
    if branch_pos == 1:
        branches.append([x0-1,branch_height+1,z0-3])
        place_block(editor, x0-1, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0-1, branch_height, z0-2, Block(wood))
        place_block(editor, x0, branch_height, z0-1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0,branch_height+1,z0-3])
        place_block(editor, x0, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0, branch_height, z0-2, Block(wood))
        place_block(editor, x0, branch_height, z0-1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+1,branch_height+1,z0-3])
        place_block(editor, x0+1, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0+1, branch_height, z0-2, Block(wood))
        place_block(editor, x0, branch_height, z0-1, Block(wood))
    branch_height = randint(height-5, height-2)
    branch_pos = randint(1, 3)
    if branch_pos == 1:
        branches.append([x0-1,branch_height+1,z0+3])
        place_block(editor, x0-1, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0-1, branch_height, z0+2, Block(wood))
        place_block(editor, x0, branch_height, z0+1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0,branch_height+1,z0+3])
        place_block(editor, x0, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0, branch_height, z0+2, Block(wood))
        place_block(editor, x0, branch_height, z0+1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+1,branch_height+1,z0+3])
        place_block(editor, x0+1, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0+1, branch_height, z0+2, Block(wood))
        place_block(editor, x0, branch_height, z0+1, Block(wood))
    
    branch_num = randint(1,3)
    small_branches = []
    #small side branches
    for a in range (0, branch_num):
        branch_height = randint(int((height-y0)/2+y0), height-5)
        branch_pos = randint(1, 16)
        if branch_pos == 1:
            small_branches.append([x0+2,branch_height,z0])
            place_block(editor, x0+2, branch_height, z0, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0, Block(wood))
        elif branch_pos == 2:
            small_branches.append([x0+2,branch_height,z0+1])
            place_block(editor, x0+2, branch_height, z0+1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-1,z0+1, Block(wood))
            else:
                place_block(editor, x0+1,branch_height-1,z0, Block(wood))
        elif branch_pos == 3:
            small_branches.append([x0+2,branch_height,z0+2])
            place_block(editor, x0+2,branch_height,z0+2, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 4:
            small_branches.append([x0+2,branch_height,z0-1])
            place_block(editor, x0+2, branch_height, z0-1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-1,z0-1, Block(wood))
            else:
                place_block(editor, x0+1,branch_height-1,z0, Block(wood))
        elif branch_pos == 5:
            small_branches.append([x0+2,branch_height,z0-2])
            place_block(editor, x0+2, branch_height, z0-2, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 6:
            small_branches.append([x0-2,branch_height,z0])
            place_block(editor, x0-2, branch_height, z0, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0, Block(wood))
        elif branch_pos == 7:
            small_branches.append([x0-2,branch_height,z0+1])
            place_block(editor, x0-2,branch_height,z0+1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-1,z0+1, Block(wood))
            else:
                place_block(editor, x0-1,branch_height-1,z0, Block(wood))
        elif branch_pos == 8:
            small_branches.append([x0-2,branch_height,z0+2])
            place_block(editor, x0-2,branch_height,z0+2, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 9:
            small_branches.append([x0-2,branch_height,z0-1])
            place_block(editor, x0-2, branch_height, z0-1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-1,z0-1, Block(wood))
            else:
                place_block(editor, x0-1,branch_height-1,z0, Block(wood))
        elif branch_pos == 10:
            small_branches.append([x0-2,branch_height,z0-2])
            place_block(editor, x0-2, branch_height, z0-2, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 11:
            small_branches.append([x0+1,branch_height,z0-2])
            place_block(editor, x0+1, branch_height, z0-2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-1,z0-1, Block(wood))
            else:
                place_block(editor, x0,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 12:
            small_branches.append([x0,branch_height,z0-2])
            place_block(editor, x0, branch_height, z0-2, Block(wood))
            place_block(editor, x0, branch_height-1, z0-1, Block(wood))
        elif branch_pos == 13:
            small_branches.append([x0-1,branch_height,z0-2])
            place_block(editor, x0-1, branch_height, z0-2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-1,z0-1, Block(wood))
            else:
                place_block(editor, x0,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 14:
            small_branches.append([x0+1,branch_height,z0+2])
            place_block(editor, x0+1, branch_height, z0+2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-1,z0+1, Block(wood))
            else:
                place_block(editor, x0,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 15:
            small_branches.append([x0,branch_height,z0+2])
            place_block(editor, x0, branch_height, z0+2, Block(wood))
            place_block(editor, x0, branch_height-1, z0+1, Block(wood))
        elif branch_pos == 16:
            small_branches.append([x0-1,branch_height,z0+2])
            place_block(editor, x0-1, branch_height, z0+2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-1,z0+1, Block(wood))
            else:
                place_block(editor, x0,branch_height-1,z0+1, Block(wood))

    for branch in branches:
        x1, y1, z1 = branch[0], branch[1], branch[2]

        place_block(editor, x1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-1, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-2, Block(leaf), leaf_chance)

    for branch in small_branches:
        x1, y1, z1 = branch[0], branch[1], branch[2]

        place_block(editor, x1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-1, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-1, Block(leaf), leaf_chance)
    
def generate_large_jungle(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    x0, y0, z0 = point.x, point.y, point.z
    seed()
    height = randint(15,25)+y0
    branches = []
    
    for y in range (y0,height+1): #tree stem
        place_block(editor, x0, y, z0, Block(wood))

    branches.append([x0, height, z0])

    # random branch generation, 1 random branch for each quadrant
    branch_height = randint(height-6, height-3)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0-4,branch_height+2,z0-4])
        place_block(editor, x0-4, branch_height+2, z0-4, Block(wood))
        place_block(editor, x0-3, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0-2, branch_height, z0-2, Block(wood))
        place_block(editor, x0-1, branch_height, z0-1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-3,branch_height+2,z0-4])
        place_block(editor, x0-3, branch_height+2, z0-4, Block(wood))
        place_block(editor, x0-3, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0-2, branch_height, z0-2, Block(wood))
        place_block(editor, x0-1, branch_height, z0-1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-2,branch_height+2,z0-4])
        place_block(editor, x0-2, branch_height+2, z0-4, Block(wood))
        place_block(editor, x0-2, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0-1, branch_height, z0-2, Block(wood))
        place_block(editor, x0-1, branch_height, z0-1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0-4,branch_height+2,z0-3])
        place_block(editor, x0-4, branch_height+2, z0-3, Block(wood))
        place_block(editor, x0-3, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0-2, branch_height, z0-2, Block(wood))
        place_block(editor, x0-1, branch_height, z0-1, Block(wood))
    elif branch_pos == 5:
        branches.append([x0-4,branch_height+2,z0-2])
        place_block(editor, x0-4, branch_height+2, z0-2, Block(wood))
        place_block(editor, x0-3, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0-2, branch_height, z0-1, Block(wood))
        place_block(editor, x0-1, branch_height, z0-1, Block(wood))
    branch_height = randint(height-6, height-3)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0+4,branch_height+2,z0-4])
        place_block(editor, x0+4, branch_height+2, z0-4, Block(wood))
        place_block(editor, x0+3, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0+2, branch_height, z0-2, Block(wood))
        place_block(editor, x0+1, branch_height, z0-1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+3,branch_height+2,z0-4])
        place_block(editor, x0+3, branch_height+2, z0-4, Block(wood))
        place_block(editor, x0+3, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0+2, branch_height, z0-2, Block(wood))
        place_block(editor, x0+1, branch_height, z0-1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+2,branch_height+2,z0-4])
        place_block(editor, x0+2, branch_height+2, z0-4, Block(wood))
        place_block(editor, x0+2, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0+1, branch_height, z0-2, Block(wood))
        place_block(editor, x0+1, branch_height, z0-1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+4,branch_height+2,z0-3])
        place_block(editor, x0+4, branch_height+2, z0-3, Block(wood))
        place_block(editor, x0+3, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0+2, branch_height, z0-2, Block(wood))
        place_block(editor, x0+1, branch_height, z0-1, Block(wood))
    elif branch_pos == 5:
        branches.append([x0+4,branch_height+2,z0-2])
        place_block(editor, x0+4, branch_height+2, z0-2, Block(wood))
        place_block(editor, x0+3, branch_height+1, z0-2, Block(wood))
        place_block(editor, x0+2, branch_height, z0-1, Block(wood))
        place_block(editor, x0+1, branch_height, z0-1, Block(wood))
    branch_height = randint(height-6, height-3)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0-4,branch_height+2,z0+4])
        place_block(editor, x0-4, branch_height+2, z0+4, Block(wood))
        place_block(editor, x0-3, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0-2, branch_height, z0+2, Block(wood))
        place_block(editor, x0-1, branch_height, z0+1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-3,branch_height+2,z0+4])
        place_block(editor, x0-3, branch_height+2, z0+4, Block(wood))
        place_block(editor, x0-3, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0-2, branch_height, z0+2, Block(wood))
        place_block(editor, x0-1, branch_height, z0+1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-2,branch_height+2,z0+4])
        place_block(editor, x0-2, branch_height+2, z0+4, Block(wood))
        place_block(editor, x0-2, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0-1, branch_height, z0+2, Block(wood))
        place_block(editor, x0-1, branch_height, z0+1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0-4,branch_height+2,z0+3])
        place_block(editor, x0-4, branch_height+2, z0+3, Block(wood))
        place_block(editor, x0-3, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0-2, branch_height, z0+2, Block(wood))
        place_block(editor, x0-1, branch_height, z0+1, Block(wood))
    elif branch_pos == 5:
        branches.append([x0-4,branch_height+2,z0+2])
        place_block(editor, x0-4, branch_height+2, z0+2, Block(wood))
        place_block(editor, x0-3, branch_height+1, z0+2, Block(wood))
        place_block(editor, x0-2, branch_height, z0+1, Block(wood))
        place_block(editor, x0-1, branch_height, z0+1, Block(wood))
    branch_height = randint(height-6, height-3)
    branch_pos = randint(1, 5)
    if branch_pos == 1:
        branches.append([x0+4,branch_height+2,z0+4])
        place_block(editor, x0+4, branch_height+2, z0+4, Block(wood))
        place_block(editor, x0+3, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0+2, branch_height, z0+2, Block(wood))
        place_block(editor, x0+1, branch_height, z0+1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+3,branch_height+2,z0+4])
        place_block(editor, x0+3, branch_height+2, z0+4, Block(wood))
        place_block(editor, x0+3, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0+2, branch_height, z0+2, Block(wood))
        place_block(editor, x0+1, branch_height, z0+1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+2,branch_height+2,z0+4])
        place_block(editor, x0+2, branch_height+2, z0+4, Block(wood))
        place_block(editor, x0+2, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0+1, branch_height, z0+2, Block(wood))
        place_block(editor, x0+1, branch_height, z0+1, Block(wood))
    elif branch_pos == 4:
        branches.append([x0+4,branch_height+2,z0+3])
        place_block(editor, x0+4, branch_height+2, z0+3, Block(wood))
        place_block(editor, x0+3, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0+2, branch_height, z0+2, Block(wood))
        place_block(editor, x0+1, branch_height, z0+1, Block(wood))
    elif branch_pos == 5:
        branches.append([x0+4,branch_height+2,z0+2])
        place_block(editor, x0+4, branch_height+2, z0+2, Block(wood))
        place_block(editor, x0+3, branch_height+1, z0+2, Block(wood))
        place_block(editor, x0+2, branch_height, z0+1, Block(wood))
        place_block(editor, x0+1, branch_height, z0+1, Block(wood))

    branch_height = randint(height-6, height-3)
    branch_pos = randint(1, 3)
    if branch_pos == 1:
        branches.append([x0-4,branch_height+2,z0-1])
        place_block(editor, x0-4, branch_height+2, z0-1, Block(wood))
        place_block(editor, x0-3, branch_height+1, z0-1, Block(wood))
        place_block(editor, x0-2, branch_height, z0-1, Block(wood))
        place_block(editor, x0-1, branch_height, z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0-4,branch_height+2,z0])
        place_block(editor, x0-4, branch_height+2, z0, Block(wood))
        place_block(editor, x0-3, branch_height+1, z0, Block(wood))
        place_block(editor, x0-2, branch_height, z0, Block(wood))
        place_block(editor, x0-1, branch_height, z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0-4,branch_height+2,z0+1])
        place_block(editor, x0-4, branch_height+2, z0+1, Block(wood))
        place_block(editor, x0-3, branch_height+1, z0+1, Block(wood))
        place_block(editor, x0-2, branch_height, z0+1, Block(wood))
        place_block(editor, x0-1, branch_height, z0, Block(wood))
    branch_height = randint(height-6, height-3)
    branch_pos = randint(1, 3)
    if branch_pos == 1:
        branches.append([x0+4,branch_height+2,z0-1])
        place_block(editor, x0+4, branch_height+2, z0-1, Block(wood))
        place_block(editor, x0+3, branch_height+1, z0-1, Block(wood))
        place_block(editor, x0+2, branch_height, z0-1, Block(wood))
        place_block(editor, x0+1, branch_height, z0, Block(wood))
    elif branch_pos == 2:
        branches.append([x0+4,branch_height+2,z0])
        place_block(editor, x0+4, branch_height+2, z0, Block(wood))
        place_block(editor, x0+3, branch_height+1, z0, Block(wood))
        place_block(editor, x0+2, branch_height, z0, Block(wood))
        place_block(editor, x0+1, branch_height, z0, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+4,branch_height+2,z0+1])
        place_block(editor, x0+4, branch_height+2, z0+1, Block(wood))
        place_block(editor, x0+3, branch_height+1, z0+1, Block(wood))
        place_block(editor, x0+2, branch_height, z0+1, Block(wood))
        place_block(editor, x0+1, branch_height, z0, Block(wood))
    branch_height = randint(height-6, height-3)
    branch_pos = randint(1, 3)
    if branch_pos == 1:
        branches.append([x0-1,branch_height+2,z0+4])
        place_block(editor, x0-1, branch_height+2, z0+4, Block(wood))
        place_block(editor, x0-1, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0-1, branch_height, z0+2, Block(wood))
        place_block(editor, x0, branch_height, z0+1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0,branch_height+2,z0+4])
        place_block(editor, x0, branch_height+2, z0+4, Block(wood))
        place_block(editor, x0, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0, branch_height, z0+2, Block(wood))
        place_block(editor, x0, branch_height, z0+1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+1,branch_height+2,z0+4])
        place_block(editor, x0+1, branch_height+2, z0+4, Block(wood))
        place_block(editor, x0+1, branch_height+1, z0+3, Block(wood))
        place_block(editor, x0+1, branch_height, z0+2, Block(wood))
        place_block(editor, x0, branch_height, z0+1, Block(wood))
    branch_height = randint(height-6, height-3)
    branch_pos = randint(1, 3)
    if branch_pos == 1:
        branches.append([x0-1,branch_height+2,z0-4])
        place_block(editor, x0-1, branch_height+2, z0-4, Block(wood))
        place_block(editor, x0-1, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0-1, branch_height, z0-2, Block(wood))
        place_block(editor, x0, branch_height, z0-1, Block(wood))
    elif branch_pos == 2:
        branches.append([x0,branch_height+2,z0-4])
        place_block(editor, x0, branch_height+2, z0-4, Block(wood))
        place_block(editor, x0, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0, branch_height, z0-2, Block(wood))
        place_block(editor, x0, branch_height, z0-1, Block(wood))
    elif branch_pos == 3:
        branches.append([x0+1,branch_height+2,z0-4])
        place_block(editor, x0+1, branch_height+2, z0-4, Block(wood))
        place_block(editor, x0+1, branch_height+1, z0-3, Block(wood))
        place_block(editor, x0+1, branch_height, z0-2, Block(wood))
        place_block(editor, x0, branch_height, z0-1, Block(wood))

    branch_num = randint(2,5)
    small_branches = []
    #small lower branches
    for a in range (0, branch_num):
        branch_height = randint(int((height-y0)/2+y0), height-7)
        branch_pos = randint(1, 24)
        if branch_pos == 1:
            small_branches.append([x0+3,branch_height,z0])
            place_block(editor, x0+3, branch_height, z0, Block(wood))
            place_block(editor, x0+2, branch_height-1, z0, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0, Block(wood))
        elif branch_pos == 2:
            small_branches.append([x0+3,branch_height,z0+1])
            place_block(editor, x0+3,branch_height,z0+1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+2,branch_height-1,z0+1, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-1,z0, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0, Block(wood))
        elif branch_pos == 3:
            small_branches.append([x0+3,branch_height,z0+2])
            place_block(editor, x0+3,branch_height,z0+2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+2,branch_height-1,z0+1, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 4:
            small_branches.append([x0+3,branch_height,z0+3])
            place_block(editor, x0+3, branch_height, z0+3, Block(wood))
            place_block(editor, x0+2, branch_height-1, z0+2, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0+1, Block(wood))  
        elif branch_pos == 5:
            small_branches.append([x0+2,branch_height,z0+3])
            place_block(editor, x0+2,branch_height,z0+3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+2,branch_height-1,z0+2, Block(wood))
            else:
                place_block(editor, x0+1,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 6:
            small_branches.append([x0+1,branch_height,z0+3])
            place_block(editor, x0+1,branch_height,z0+3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-1,z0+2, Block(wood))
            else:
                place_block(editor, x0,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 7:
            small_branches.append([x0,branch_height,z0+3])
            place_block(editor, x0, branch_height, z0+3, Block(wood))
            place_block(editor, x0, branch_height-1, z0+2, Block(wood))
            place_block(editor, x0, branch_height-1, z0+1, Block(wood))
        elif branch_pos == 8:
            small_branches.append([x0-1,branch_height,z0+3])
            place_block(editor, x0-1,branch_height,z0+3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-1,z0+2, Block(wood))
            else:
                place_block(editor, x0,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 9:
            small_branches.append([x0-2,branch_height,z0+3])
            place_block(editor, x0-2,branch_height,z0+3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-2,branch_height-1,z0+2, Block(wood))
            else:
                place_block(editor, x0-1,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 10:
            small_branches.append([x0-3,branch_height,z0+3])
            place_block(editor, x0-3, branch_height, z0+3, Block(wood))
            place_block(editor, x0-2, branch_height-1, z0+2, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0+1, Block(wood)) 
        elif branch_pos == 11:
            small_branches.append([x0-3,branch_height,z0+2])
            place_block(editor, x0-3,branch_height,z0+2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-2,branch_height-1,z0+1, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-1,z0+2, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0+1, Block(wood))
        elif branch_pos == 12:
            small_branches.append([x0-3,branch_height,z0+1])
            place_block(editor, x0-3,branch_height,z0+1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-2,branch_height-1,z0+1, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-1,z0, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0, Block(wood))
        elif branch_pos == 13:
            small_branches.append([x0-3,branch_height,z0])
            place_block(editor, x0-3, branch_height, z0, Block(wood))
            place_block(editor, x0-2, branch_height-1, z0, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0, Block(wood))
        elif branch_pos == 14:
            small_branches.append([x0-3,branch_height,z0-1])
            place_block(editor, x0-3,branch_height,z0-1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-2,branch_height-1,z0-1, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-1,z0, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0, Block(wood))
        elif branch_pos == 15:
            small_branches.append([x0-3,branch_height,z0-2])
            place_block(editor, x0-3,branch_height,z0-2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-2,branch_height-1,z0-1, Block(wood))
            else:
                place_block(editor, x0-2,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 16:
            small_branches.append([x0-3,branch_height,z0-3])
            place_block(editor, x0-3, branch_height, z0-3, Block(wood))
            place_block(editor, x0-2, branch_height-1, z0-2, Block(wood))
            place_block(editor, x0-1, branch_height-1, z0-1, Block(wood)) 
        elif branch_pos == 17:
            small_branches.append([x0-2,branch_height,z0-3])
            place_block(editor, x0-2,branch_height,z0-3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-2,branch_height-1,z0-2, Block(wood))
            else:
                place_block(editor, x0-1,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0-1,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 18:
            small_branches.append([x0-1,branch_height,z0-3])
            place_block(editor, x0-1,branch_height,z0-3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0-1,branch_height-1,z0-2, Block(wood))
            else:
                place_block(editor, x0,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 19:
            small_branches.append([x0,branch_height,z0-3])
            place_block(editor, x0, branch_height, z0-3, Block(wood))
            place_block(editor, x0, branch_height-1, z0-2, Block(wood))
            place_block(editor, x0, branch_height-1, z0-1, Block(wood))
        elif branch_pos == 20:
            small_branches.append([x0+1,branch_height,z0-3])
            place_block(editor, x0+1,branch_height,z0-3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+1,branch_height-1,z0-2, Block(wood))
            else:
                place_block(editor, x0,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 21:
            small_branches.append([x0+2,branch_height,z0-3])
            place_block(editor, x0+2,branch_height,z0-3, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+2,branch_height-1,z0-2, Block(wood))
            else:
                place_block(editor, x0+1,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 22:
            small_branches.append([x0+3,branch_height,z0-3])
            place_block(editor, x0+3, branch_height, z0-3, Block(wood))
            place_block(editor, x0+2, branch_height-1, z0-2, Block(wood))
            place_block(editor, x0+1, branch_height-1, z0-1, Block(wood))
        elif branch_pos == 23:
            small_branches.append([x0+3,branch_height,z0-2])
            place_block(editor, x0+3,branch_height,z0-2, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+2,branch_height-1,z0-1, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-1,z0-2, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0-1, Block(wood))
        elif branch_pos == 24:
            small_branches.append([x0+3,branch_height,z0-1])
            place_block(editor, x0+3,branch_height,z0-1, Block(wood))
            b = randint(1,2)
            if b==1:
                place_block(editor, x0+2,branch_height-1,z0-1, Block(wood))
            else:
                place_block(editor, x0+2,branch_height-1,z0, Block(wood))
            place_block(editor, x0+1,branch_height-1,z0, Block(wood))

    for branch in branches:
        x1, y1, z1 = branch[0], branch[1], branch[2]

        place_block(editor, x1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-2, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+3, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-3, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+3, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-3, Block(leaf), leaf_chance)
        place_block(editor, x1+3, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-3, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1+3, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-3, Block(leaf), leaf_chance)
        place_block(editor, x1+3, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-3, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+3, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-3, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1-2, Block(leaf), leaf_chance)

    for branch in small_branches:
        x1, y1, z1 = branch[0], branch[1], branch[2]

        place_block(editor, x1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1+1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1+1, z1-1, Block(leaf), leaf_chance)

        place_block(editor, x1+1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1+1, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1+1, y1, z1-2, Block(leaf), leaf_chance)
        place_block(editor, x1+2, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-2, y1, z1-1, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1+2, Block(leaf), leaf_chance)
        place_block(editor, x1-1, y1, z1-2, Block(leaf), leaf_chance)
    
def generate_mega_jungle(point: ivec3, editor, wood: str, leaf: str, leaf_chance: int=100):
    generate_large_jungle(point, editor, wood, leaf, leaf_chance)
    x0, y0, z0 = point.x, point.y, point.z
    new_point = ivec3(x0+1, y0, z0)
    generate_large_jungle(new_point, editor, wood, leaf, leaf_chance)
    new_point = ivec3(x0+1, y0, z0+1)
    generate_large_jungle(new_point, editor, wood, leaf, leaf_chance)
    new_point = ivec3(x0, y0, z0+1)
    generate_large_jungle(new_point, editor, wood, leaf, leaf_chance)