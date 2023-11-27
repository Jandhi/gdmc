from core.structures.market.stall import *
from gdpc import Editor, Block
from random import seed
from random import randint
from core.structures.legacy_directions import north, east, west, south, left, right, to_text, opposite
from core.utils.setblock import place_block, summon_entity
from gdpc.vector_tools import ivec3

class StallGenerator():
    name = 'Stall Generator'
    stalls : Stall = []

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    def generate(self, editor : Editor):
        if not self.stalls:
            return

        for stall in self.stalls:
            self.generate_stall(stall, editor)

    def generate_stall(self, stall, editor):
        #dealing with directionality
        x0, y0, z0 = stall.get_origin()
        (swap, l0, l_dir, d0, d_dir) = self.setup_direction(stall)

        self.generate_base(stall, editor)
        self.generate_counter(stall, editor)
        self.generate_side(stall, editor)
        self.generate_roof(stall, editor)
        self.generate_overhang(stall, editor)
        if stall.back_counter:
            if swap:
                stall.set_origin((x0+(stall.depth-1)*d_dir,y0,z0+(stall.length-1)*l_dir))
            else:
                stall.set_origin((x0+(stall.length-1)*l_dir,y0,z0+(stall.depth-1)*d_dir))
            stall.set_direction(opposite(stall.direction))
            self.generate_counter(stall, editor)
            # reseting changes
            stall.set_origin((x0, y0, z0))
            stall.set_direction(opposite(stall.direction))
        if stall.goods!=None:
            self.generate_goods(stall, editor)
    
    def get_direction(self, direction):
        if direction == east:
            return (-1,1)
        elif direction == west:
            return (1,-1)
        elif direction == north:
            return (1,1)
        elif direction == south:
            return (-1,-1)

    def setup_direction(self, stall):
        x0, y0, z0 = stall.get_origin()
        (x_dir,z_dir) = self.get_direction(stall.direction)
        swap = (not x_dir==z_dir)
        if swap: #swapping length and depth to deal with east west directional stalls
            l0 = z0
            l_dir = z_dir
            d0 = x0
            d_dir = x_dir 
        else:
            l0 = x0
            l_dir = x_dir
            d0 = z0
            d_dir = z_dir 
        return (swap, l0, l_dir, d0, d_dir)

    def generate_base(self, stall, editor):
        x0, y0, z0 = stall.get_origin()
        (x_dir,z_dir) = self.get_direction(stall.direction)
        swap = (x_dir==z_dir)
        corners = []
        corners.append([x0,y0,z0])
        if swap:
            corners.append([x0+(stall.length-1)*x_dir,y0,z0])
            corners.append([x0,y0,z0+(stall.depth-1)*z_dir])
            corners.append([x0+(stall.length-1)*x_dir,y0,z0+(stall.depth-1)*z_dir])
            stall.add_floor_space((x0,y0,z0-z_dir))
            stall.add_floor_space((x0+(stall.length-1)*x_dir,y0,z0-z_dir))
        else:
            corners.append([x0+(stall.depth-1)*x_dir,y0,z0])
            corners.append([x0,y0,z0+(stall.length-1)*z_dir])
            corners.append([x0+(stall.depth-1)*x_dir,y0,z0+(stall.length-1)*z_dir])
            stall.add_floor_space((x0-x_dir,y0,z0))
            stall.add_floor_space((x0-x_dir,y0,z0+(stall.length-1)*z_dir))
        for corner in corners:
            editor.placeBlock((corner[0], corner[1], corner[2]), Block('minecraft:oak_planks'))
            for a in range(corner[1]+1, corner[1]+stall.height-1):
                editor.placeBlock((corner[0], a, corner[2]), Block('minecraft:oak_fence'))

    def generate_counter(self, stall, editor):
        x0, y0, z0 = stall.get_origin()
        (swap, l0, l_dir, d0, d_dir) = self.setup_direction(stall)
        if stall.counter == BASIC:
            for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                if swap:
                    editor.placeBlock((x0, y0, a), Block('minecraft:oak_planks'))
                    stall.add_counter_space((x0,y0+1,a))
                else: 
                    editor.placeBlock((a, y0, z0), Block('minecraft:oak_planks'))
                    stall.add_counter_space((a,y0+1,z0))
        elif stall.counter == HALF_STAIR:
            if stall.length%2==0:
                for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                    if (a-l0)%2==0 and a<=stall.length-2:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block('minecraft:oak_planks'))
                            stall.add_counter_space((x0,y0+1,a))
                        else: 
                            editor.placeBlock((a, y0, z0), Block('minecraft:oak_planks'))
                            stall.add_counter_space((a,y0+1,z0))
                    elif (a-l0)%2==1 and a>=stall.length-2:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block('minecraft:oak_planks'))
                            stall.add_counter_space((x0,y0+1,a))
                        else: 
                            editor.placeBlock((a, y0, z0), Block('minecraft:oak_planks'))
                            stall.add_counter_space((a,y0+1,z0))
                    else:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block(f'minecraft:oak_stairs[facing={to_text(opposite(stall.direction))}, half=top]'))
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            editor.placeBlock((a, y0, z0), Block(f'minecraft:oak_stairs[facing={to_text(opposite(stall.direction))}, half=top]'))
                            stall.add_counter_space((a,y0+1,z0))
            else:
                for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                    if (a-l0)%2==0:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block('minecraft:oak_planks'))
                            stall.add_counter_space((x0,y0+1,a))
                        else: 
                            editor.placeBlock((a, y0, z0), Block('minecraft:oak_planks'))
                            stall.add_counter_space((a,y0+1,z0))
                    else:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block(f'minecraft:oak_stairs[facing={to_text(opposite(stall.direction))}, half=top]'))
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            editor.placeBlock((a, y0, z0), Block(f'minecraft:oak_stairs[facing={to_text(opposite(stall.direction))}, half=top]'))
                            stall.add_counter_space((a,y0+1,z0))
        elif stall.counter == STAIR:
            for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                if swap:
                    editor.placeBlock((x0, y0, a), Block(f'minecraft:oak_stairs[facing={to_text(opposite(stall.direction))}, half=top]'))
                    stall.add_counter_space((x0,y0+1,a))
                else:
                    editor.placeBlock((a, y0, z0), Block(f'minecraft:oak_stairs[facing={to_text(opposite(stall.direction))}, half=top]'))
                    stall.add_counter_space((a,y0+1,z0))
        elif stall.counter == SLAB:
            for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                if swap:
                    editor.placeBlock((x0, y0, a), Block('minecraft:oak_slab[type=top]'))
                    stall.add_counter_space((x0,y0+1,a))
                else:
                    editor.placeBlock((a, y0, z0), Block('minecraft:oak_slab[type=top]'))
                    stall.add_counter_space((a,y0+1,z0))
        elif stall.counter == HALF_SLAB:
            if stall.length%2==0:
                for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                    if (a-l0)%2==0 and a<=stall.length-2:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block('minecraft:oak_planks'))
                            stall.add_counter_space((x0,y0+1,a))
                        else: 
                            editor.placeBlock((a, y0, z0), Block('minecraft:oak_planks'))
                            stall.add_counter_space((a,y0+1,z0))
                    elif (a-l0)%2==1 and a>=stall.length-2:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block('minecraft:oak_planks'))
                            stall.add_counter_space((x0,y0+1,a))
                        else: 
                            editor.placeBlock((a, y0, z0), Block('minecraft:oak_planks'))
                            stall.add_counter_space((a,y0+1,z0))
                    else:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block('minecraft:oak_slab[type=top]'))
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            editor.placeBlock((a, y0, z0), Block('minecraft:oak_slab[type=top]'))
                            stall.add_counter_space((a,y0+1,z0))
            else:
                for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                    if (a-l0)%2==0:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block('minecraft:oak_planks'))
                            stall.add_counter_space((x0,y0+1,a))
                        else: 
                            editor.placeBlock((a, y0, z0), Block('minecraft:oak_planks'))
                            stall.add_counter_space((a,y0+1,z0))
                    else:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block('minecraft:oak_slab[type=top]'))
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            editor.placeBlock((a, y0, z0), Block('minecraft:oak_slab[type=top]'))
                            stall.add_counter_space((a,y0+1,z0))
        elif stall.counter == STAIR_SLAB:
            if stall.length%2==0:
                for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                    if (a-l0)%2==0 and a<=stall.length-2:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block(f'minecraft:oak_stairs[facing={to_text(opposite(stall.direction))}, half=top]'))
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            editor.placeBlock((a, y0, z0), Block(f'minecraft:oak_stairs[facing={to_text(opposite(stall.direction))}, half=top]'))
                            stall.add_counter_space((a,y0+1,z0))
                    elif (a-l0)%2==1 and a>=stall.length-2:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block(f'minecraft:oak_stairs[facing={to_text(opposite(stall.direction))}, half=top]'))
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            editor.placeBlock((a, y0, z0), Block(f'minecraft:oak_stairs[facing={to_text(opposite(stall.direction))}, half=top]'))
                            stall.add_counter_space((a,y0+1,z0))
                    else:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block('minecraft:oak_slab[type=top]'))
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            editor.placeBlock((a, y0, z0), Block('minecraft:oak_slab[type=top]'))
                            stall.add_counter_space((a,y0+1,z0))
            else:
                for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                    if (a-l0)%2==0:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block(f'minecraft:oak_stairs[facing={to_text(opposite(stall.direction))}, half=top]'))
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            editor.placeBlock((a, y0, z0), Block(f'minecraft:oak_stairs[facing={to_text(opposite(stall.direction))}, half=top]'))
                            stall.add_counter_space((a,y0+1,z0))
                    else:
                        if swap:
                            editor.placeBlock((x0, y0, a), Block('minecraft:oak_slab[type=top]'))
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            editor.placeBlock((a, y0, z0), Block('minecraft:oak_slab[type=top]'))
                            stall.add_counter_space((a,y0+1,z0))

    def generate_side(self, stall, editor):
        x0, y0, z0 = stall.get_origin()
        (swap, l0, l_dir, d0, d_dir) = self.setup_direction(stall)
        if stall.side == None:
            return
        elif stall.side == BASIC: 
            for a in range(d0+1*d_dir,d0+(stall.depth-1)*d_dir, d_dir):
                if swap:
                    editor.placeBlock((a, y0, z0), Block('minecraft:oak_planks'))
                    editor.placeBlock((a, y0, z0+(stall.length-1)*l_dir), Block('minecraft:oak_planks'))
                    stall.add_counter_space((a,y0+1,z0))
                    stall.add_counter_space((a,y0+1,z0+(stall.length-1)*l_dir))
                else:
                    editor.placeBlock((x0, y0, a), Block('minecraft:oak_planks'))
                    editor.placeBlock((x0+(stall.length-1)*l_dir, y0, a), Block('minecraft:oak_planks'))
                    stall.add_counter_space((x0,y0+1,a))
                    stall.add_counter_space((x0+(stall.length-1)*l_dir,y0+1,a))
        elif stall.side == FENCE: 
            for a in range(d0+1*d_dir,d0+(stall.depth-1)*d_dir, d_dir):
                if swap:
                    editor.placeBlock((a, y0, z0), Block(f'minecraft:oak_fence[{to_text(opposite(stall.direction))}=true,{to_text(stall.direction)}=true]'))
                    editor.placeBlock((a, y0, z0+(stall.length-1)*l_dir), Block(f'minecraft:oak_fence[{to_text(opposite(stall.direction))}=true,{to_text(stall.direction)}=true]'))
                else:
                    editor.placeBlock((x0, y0, a), Block(f'minecraft:oak_fence[{to_text(opposite(stall.direction))}=true,{to_text(stall.direction)}=true]'))
                    editor.placeBlock((x0+(stall.length-1)*l_dir, y0, a), Block(f'minecraft:oak_fence[{to_text(opposite(stall.direction))}=true,{to_text(stall.direction)}=true]'))
        elif stall.side == FENCE_GATE: 
            for a in range(d0+1*d_dir,d0+(stall.depth-1)*d_dir, d_dir):
                if swap:
                    editor.placeBlock((a, y0, z0), Block(f'minecraft:oak_fence_gate[facing={to_text(right[stall.direction])}]'))
                    editor.placeBlock((a, y0, z0+(stall.length-1)*l_dir), Block(f'minecraft:oak_fence_gate[facing={to_text(right[stall.direction])}]'))
                else:
                    editor.placeBlock((x0, y0, a), Block(f'minecraft:oak_fence_gate[facing={to_text(right[stall.direction])}]'))
                    editor.placeBlock((x0+(stall.length-1)*l_dir, y0, a), Block(f'minecraft:oak_fence_gate[facing={to_text(right[stall.direction])}]'))
        elif stall.side == TRAPDOOR:
            for a in range(d0+1*d_dir,d0+(stall.depth-1)*d_dir, d_dir):
                if swap:
                    editor.placeBlock((a, y0, z0), Block(f'minecraft:oak_trapdoor[facing={to_text(opposite(stall.direction))}, half=top]'))
                    editor.placeBlock((a, y0, z0+(stall.length-1)*l_dir), Block(f'minecraft:oak_trapdoor[facing={to_text(stall.direction)}, half=top]'))
                else: 
                    editor.placeBlock((x0, y0, a), Block(f'minecraft:oak_trapdoor[facing={to_text(opposite(stall.direction))}, half=top]'))
                    editor.placeBlock((x0+(stall.length-1)*l_dir, y0, a), Block(f'minecraft:oak_trapdoor[facing={to_text(stall.direction)}, half=top]'))
        elif stall.side == STAIR: 
            for a in range(d0+1*d_dir,d0+(stall.depth-1)*d_dir, d_dir):
                if swap:
                    editor.placeBlock((a, y0, z0), Block(f'minecraft:oak_stairs[facing={to_text(right[stall.direction])}, half=top]'))
                    editor.placeBlock((a, y0, z0+(stall.length-1)*l_dir), Block(f'minecraft:oak_stairs[facing={to_text(left[stall.direction])}, half=top]'))
                    stall.add_counter_space((a,y0+1,z0))
                    stall.add_counter_space((a,y0+1,z0+(stall.length-1)*l_dir))
                else:
                    editor.placeBlock((x0, y0, a), Block(f'minecraft:oak_stairs[facing={to_text(right[stall.direction])}, half=top]'))
                    editor.placeBlock((x0+(stall.length-1)*l_dir, y0, a), Block(f'minecraft:oak_stairs[facing={to_text(left[stall.direction])}, half=top]'))
                    stall.add_counter_space((x0,y0+1,a))
                    stall.add_counter_space((x0+(stall.length-1)*l_dir,y0+1,a))
        elif stall.side == SLAB: 
            for a in range(d0+1*d_dir,d0+(stall.depth-1)*d_dir, d_dir):
                if swap:
                    editor.placeBlock((a, y0, z0), Block('minecraft:oak_slab[type=top]'))
                    editor.placeBlock((a, y0, z0+(stall.length-1)*l_dir), Block('minecraft:oak_slab[type=top]'))
                    stall.add_counter_space((a,y0+1,z0))
                    stall.add_counter_space((a,y0+1,z0+(stall.length-1)*l_dir))
                else:
                    editor.placeBlock((x0, y0, a), Block('minecraft:oak_slab[type=top]'))
                    editor.placeBlock((x0+(stall.length-1)*l_dir, y0, a), Block('minecraft:oak_slab[type=top]'))
                    stall.add_counter_space((x0,y0+1,a))
                    stall.add_counter_space((x0+(stall.length-1)*l_dir,y0+1,a))

    def generate_roof(self, stall, editor):
        x0, y0, z0 = stall.get_origin()
        (swap, l0, l_dir, d0, d_dir) = self.setup_direction(stall)
        if stall.roof == BASIC:
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                for b in range(d0,d0+stall.depth*d_dir, d_dir):
                    if (a-l0)%2==0:
                        if swap:
                            editor.placeBlock((b, y0+stall.height-1, a), Block(stall.palette['market_wool_1']))
                        else:
                            editor.placeBlock((a, y0+stall.height-1, b), Block(stall.palette['market_wool_1']))
                    else:
                        if swap:
                            editor.placeBlock((b, y0+stall.height-1, a), Block(stall.palette['market_wool_2']))
                        else:
                            editor.placeBlock((a, y0+stall.height-1, b), Block(stall.palette['market_wool_2']))
        elif stall.roof == BACK_DOWN:
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                for b in range(d0,d0+stall.depth*d_dir, d_dir):
                    if (a-l0)%2==0:
                        if b == (stall.depth-1)*l_dir:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-2, a), Block(stall.palette['market_wool_1']))
                            else:
                                editor.placeBlock((a, y0+stall.height-2, b), Block(stall.palette['market_wool_1']))
                        else:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-1, a), Block(stall.palette['market_wool_1']))
                            else:
                                editor.placeBlock((a, y0+stall.height-1, b), Block(stall.palette['market_wool_1']))
                    else:
                        if b == (stall.depth-1)*l_dir:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-2, a), Block(stall.palette['market_wool_2']))
                            else:
                                editor.placeBlock((a, y0+stall.height-2, b), Block(stall.palette['market_wool_2']))
                        else:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-1, a), Block(stall.palette['market_wool_2']))
                            else:
                                editor.placeBlock((a, y0+stall.height-1, b), Block(stall.palette['market_wool_2']))
        elif stall.roof == SIDES_DOWN:
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                for b in range(d0,d0+stall.depth*d_dir, d_dir):
                    if (a-l0)%2==0:
                        if a == l0+(stall.length-1)*l_dir or a==l0:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-2, a), Block(stall.palette['market_wool_1']))
                            else:
                                editor.placeBlock((a, y0+stall.height-2, b), Block(stall.palette['market_wool_1']))
                        else:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-1, a), Block(stall.palette['market_wool_1']))
                            else:
                                editor.placeBlock((a, y0+stall.height-1, b), Block(stall.palette['market_wool_1']))
                    else:
                        if a == l0+(stall.length-1)*l_dir or a==l0:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-2, a), Block(stall.palette['market_wool_2']))
                            else:
                                editor.placeBlock((a, y0+stall.height-2, b), Block(stall.palette['market_wool_2']))
                        else:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-1, a), Block(stall.palette['market_wool_2']))
                            else:
                                editor.placeBlock((a, y0+stall.height-1, b), Block(stall.palette['market_wool_2']))
        elif stall.roof == FRONT_DOWN:
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                for b in range(d0,d0+stall.depth*d_dir, d_dir):
                    if (a-l0)%2==0:
                        if b==d0:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-2, a), Block(stall.palette['market_wool_1']))
                            else:
                                editor.placeBlock((a, y0+stall.height-2, b), Block(stall.palette['market_wool_1']))
                        else:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-1, a), Block(stall.palette['market_wool_1']))
                            else:
                                editor.placeBlock((a, y0+stall.height-1, b), Block(stall.palette['market_wool_1']))
                    else:
                        if b==d0:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-2, a), Block(stall.palette['market_wool_2']))
                            else:
                                editor.placeBlock((a, y0+stall.height-2, b), Block(stall.palette['market_wool_2']))
                        else:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-1, a), Block(stall.palette['market_wool_2']))
                            else:
                                editor.placeBlock((a, y0+stall.height-1, b), Block(stall.palette['market_wool_2']))
        elif stall.roof == FRONT_BACK_DOWN:
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                for b in range(d0,d0+stall.depth*d_dir, d_dir):
                    if (a-l0)%2==0:
                        if b == d0+(stall.depth-1)*l_dir or b==d0:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-2, a), Block(stall.palette['market_wool_1']))
                            else:
                                editor.placeBlock((a, y0+stall.height-2, b), Block(stall.palette['market_wool_1']))
                        else:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-1, a), Block(stall.palette['market_wool_1']))
                            else:
                                editor.placeBlock((a, y0+stall.height-1, b), Block(stall.palette['market_wool_1']))
                    else:
                        if b == d0+(stall.depth-1)*l_dir or b==d0:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-2, a), Block(stall.palette['market_wool_2']))
                            else:
                                editor.placeBlock((a, y0+stall.height-2, b), Block(stall.palette['market_wool_2']))
                        else:
                            if swap:
                                editor.placeBlock((b, y0+stall.height-1, a), Block(stall.palette['market_wool_2']))
                            else:
                                editor.placeBlock((a, y0+stall.height-1, b), Block(stall.palette['market_wool_2']))


    def generate_overhang(self, stall, editor):
        x0, y0, z0 = stall.get_origin()
        (swap, l0, l_dir, d0, d_dir) = self.setup_direction(stall)
        if stall.overhang == None:
            return
        elif stall.overhang == TRAPDOOR:
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                if stall.roof == 'front_back_down' or stall.roof == 'front_down' or (stall.roof == 'sides_down' and (a == l0 or a == l0+(stall.length-1)*l_dir)):
                    if swap:
                        editor.placeBlock((x0-1*d_dir, y0+stall.height-2, a), Block(f'minecraft:oak_trapdoor[facing={to_text(stall.direction)}]'))
                    else:
                        editor.placeBlock((a, y0+stall.height-2, z0-1*d_dir), Block(f'minecraft:oak_trapdoor[facing={to_text(stall.direction)}]'))
                else:
                    if swap:
                        editor.placeBlock((x0-1*d_dir, y0+stall.height-1, a), Block(f'minecraft:oak_trapdoor[facing={to_text(stall.direction)}]'))
                    else:
                        editor.placeBlock((a, y0+stall.height-1, z0-1*d_dir), Block(f'minecraft:oak_trapdoor[facing={to_text(stall.direction)}]'))
        elif stall.overhang == BANNER:
            banner1 = stall.palette['market_banner_1']
            banner2 = stall.palette['market_banner_2']
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                if (a-x0)%2==0:
                    if stall.roof == 'front_back_down' or stall.roof == 'front_down' or (stall.roof == 'sides_down' and (a == l0 or a == l0+(stall.length-1)*l_dir)):
                        if swap:
                            editor.placeBlock((x0-1*d_dir, y0+stall.height-2, a), Block(f'{banner2}[facing={to_text(stall.direction)}]'))
                        else:
                            editor.placeBlock((a, y0+stall.height-2, z0-1*d_dir), Block(f'{banner1}[facing={to_text(stall.direction)}]'))
                    else:
                        if swap:
                            editor.placeBlock((x0-1*d_dir, y0+stall.height-1, a), Block(f'{banner2}[facing={to_text(stall.direction)}]'))
                        else:
                            editor.placeBlock((a, y0+stall.height-1, z0-1*d_dir), Block(f'{banner1}[facing={to_text(stall.direction)}]'))
                else:
                    if stall.roof == 'front_back_down' or stall.roof == 'front_down' or (stall.roof == 'sides_down' and (a == l0 or a == l0+(stall.length-1)*l_dir)):
                        if swap:
                            editor.placeBlock((x0-1*d_dir, y0+stall.height-2, a), Block(f'{banner1}[facing={to_text(stall.direction)}]'))
                        else:
                            editor.placeBlock((a, y0+stall.height-2, z0-1*d_dir), Block(f'{banner2}[facing={to_text(stall.direction)}]'))
                    else:
                        if swap:
                            editor.placeBlock((x0-1*d_dir, y0+stall.height-1, a), Block(f'{banner1}[facing={to_text(stall.direction)}]'))
                        else:
                            editor.placeBlock((a, y0+stall.height-1, z0-1*d_dir), Block(f'{banner2}[facing={to_text(stall.direction)}]'))
        elif stall.overhang == CAMPFIRE:
            campfire_block = 'campfire[lit=false]'
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                if stall.roof == 'front_back_down' or stall.roof == 'front_down' or (stall.roof == 'sides_down' and (a == l0 or a == l0+(stall.length-1)*l_dir)):
                    if swap:
                        editor.placeBlock((x0-1*d_dir, y0+stall.height-2, a), Block(campfire_block))
                    else:
                        editor.placeBlock((a, y0+stall.height-2, z0-1*d_dir), Block(campfire_block))
                else:
                    if swap:
                        editor.placeBlock((x0-1*d_dir, y0+stall.height-1, a), Block(campfire_block))
                    else:
                        editor.placeBlock((a, y0+stall.height-1, z0-1*d_dir), Block(campfire_block))

    def generate_goods(self, stall, editor):
        seed()
        for point in stall.counter_space:
            x, y, z = point
            generation_chance = randint(1, 4)
            if generation_chance < 4:
                good = stall.get_counter_good()
                if good[:11] == 'player_head': #player head direction
                    place_block(good, editor, ivec3(x,y,z), stall.direction)
                else:
                    editor.placeBlock((x, y, z), Block(f'minecraft:{good}'))
        
        if stall.has_floor_goods():
            for point in stall.floor_space:
                x, y, z = point
                generation_chance = randint(1, 4)
                if generation_chance < 4:
                    good = stall.get_floor_good()
                    if good[:11] == 'armor_stand': #armour stand rotation
                        id = good[:11]
                        nbt = good[11:]
                        summon_entity(id, nbt, editor, ivec3(x,y,z), stall.direction)
                    else:
                        editor.placeBlock((x, y, z), Block(f'minecraft:{good}'))