from core.structures.market.stall_generator import StallGenerator
from core.structures.market.stall import Stall
from gdpc import Editor
from gdpc.vector_tools import ivec3

class Small_Market():
    name = 'Small Market'
    origin = ivec3(0,0,0)

    def __init__(self, point: ivec3) -> None:
        self.origin = point

    def build(self, editor: Editor):

        x, y, z = self.origin
        self.stalls = []
        self.stalls.append(Stall((x+9, y, z+4),'half_stair','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall((x+9, y, z+10),'half_stair','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall((x+9, y, z+16),'half_stair','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall((x+3, y, z),'half_stair','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall((x+3, y, z+6),'half_stair','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall((x+3, y, z+12),'half_stair','trapdoor','sides_down','trapdoor','x_plus'))
        
        StallGenerator(stalls=self.stalls).generate(editor)

class Market():
    name = 'Market'
    origin = ivec3(0,0,0)

    def __init__(self, point: ivec3) -> None:
        self.origin = point

    def build(self, editor: Editor):

        x, y, z = self.origin
        self.stalls = []
        self.stalls.append(Stall((x+5, y, z+4),'random','trapdoor','sides_down','trapdoor','z_plus'))
        self.stalls.append(Stall((x+15, y, z+4),'random','trapdoor','sides_down','trapdoor','z_plus', 7))
        self.stalls.append(Stall((x+23, y, z+4),'random','trapdoor','sides_down','trapdoor','z_plus'))

        self.stalls.append(Stall((x+1, y, z+28),'random','trapdoor','sides_down','trapdoor','z_minus'))
        self.stalls.append(Stall((x+9, y, z+28),'random','trapdoor','sides_down','trapdoor','z_minus', 7))
        self.stalls.append(Stall((x+19, y, z+28),'random','trapdoor','sides_down','trapdoor','z_minus'))

        self.stalls.append(Stall((x+14, y, z+11),'random','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall((x+14, y, z+19),'random','trapdoor','sides_down','trapdoor','x_minus', 7))
        self.stalls.append(Stall((x+14, y, z+25),'random','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall((x+20, y, z+11),'random','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall((x+20, y, z+19),'random','trapdoor','sides_down','trapdoor','x_minus', 7))
        self.stalls.append(Stall((x+20, y, z+25),'random','trapdoor','sides_down','trapdoor','x_minus'))

        self.stalls.append(Stall((x+4, y, z+7),'random','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall((x+4, y, z+13),'random','trapdoor','sides_down','trapdoor','x_plus', 7))
        self.stalls.append(Stall((x+4, y, z+21),'random','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall((x+10, y, z+7),'random','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall((x+10, y, z+13),'random','trapdoor','sides_down','trapdoor','x_plus', 7))
        self.stalls.append(Stall((x+10, y, z+21),'random','trapdoor','sides_down','trapdoor','x_plus'))
        
        StallGenerator(stalls=self.stalls).generate(editor)
