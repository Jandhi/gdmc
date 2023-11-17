# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\core\\noise\\tests')

# Actual file
from core.noise.rng import RNG

def run_hash_collision_test(seed_num, iterations, modulo=-1):
    for i in range(seed_num):
        rng = RNG(i)
        numbers = set()
        collisions = 0

        for _ in range(iterations):
            val = rng.next()

            if modulo != -1:
                val %= modulo

            if val in numbers:
                collisions += 1
            else:
                numbers.add(val)
        
        if collisions > 0:
            print(f'Seed {i} has {collisions} collisions')

run_hash_collision_test(
    seed_num=10,
    iterations=1000,
    modulo=100000,
)