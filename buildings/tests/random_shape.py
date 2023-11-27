from gdpc.vector_tools import ivec2, ivec3
from core.noise.rng import RNG

def random_shape(SEED : int):
    # RANDOM
    shape = []
    heights = {}
    rand = RNG(SEED, 'random_points')

    for i in range(20):
        point = ivec2(
            rand.randrange(-2, 2), 
            rand.randrange(-2, 2)
        )

        y = 0

        if point not in heights:
            heights[point] = 1
        else:
            y = heights[point]
            heights[point] += 1

        shape.append(ivec3(point.x, y, point.y))
    
    return shape