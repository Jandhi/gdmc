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