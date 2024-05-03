from gdpc import vector_tools
from glm import vec2, fract

BITNOISE1 = 0x85297a4d
BITNOISE2 = 0x68e31da4
BITNOISE3 = 0x1859c4e9
BITNOISE4 = 0x0c1fc20b

# hashes together a seed and a position
def hash(seed : int, pos : int) -> int:
    noise = pos
    noise = noise * BITNOISE1
    noise = noise + seed
    noise = noise ^ (noise >> 8)
    noise = noise + BITNOISE2
    noise = noise ^ (noise << 8)
    noise = noise * BITNOISE3
    noise = noise ^ (noise >> 8)

    # mask to reduce size of integer
    # otherwise python will start making larger and larger sizes
    noise = noise & 0xFFFFFFFF 
    
    return noise 

# hashes together a seed with any amount of arguments
def recursive_hash(seed : int, *args : int):
    for arg in args:
        seed = hash(seed, arg)
    
    return seed

# hashes a string based on a seed
def hash_string(seed, string : str) -> int:
    return recursive_hash(seed, *(ord(letter) for letter in string))

# hashes a vec2 into a vec2
def hash22(n: vec2) -> vec2:
    k = vec2(35.131578, 12.987154)
    n = n * k + k.yx
    n = 16.0 * k * fract(n.x * n.y * (n.x + n.y))
    n = vec2(fract(n.x), fract(n.y))
    return vec2(n.x * 2.0 - 1.0, n.y * 2.0 - 1.0)

# hashes a float into a float
def hash11(n: float) -> float:
    n = (n << 13) ^ n
    n = n * (n * n * 15731.0 + 789221.0) + 1376312589.0
    return -1.0 + 2.0 * fract(n / 1073741824.0)