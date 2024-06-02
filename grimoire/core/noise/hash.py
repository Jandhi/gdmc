BITNOISE1 = 0x85297A4D
BITNOISE2 = 0x68E31DA4
BITNOISE3 = 0x1859C4E9


# hashes together a seed and a position
# uses squirrel3 algorithm
def sq_hash(seed: int, pos: int) -> int:
    noise = pos
    noise *= BITNOISE1
    noise = noise + seed
    noise = noise ^ (noise >> 8)
    noise = noise + BITNOISE2
    noise = noise ^ (noise << 8)
    noise = noise * BITNOISE3
    noise = noise ^ (noise >> 8)

    # mask to reduce size of integer
    # otherwise python will start making larger and larger sizes
    return noise & 0xFFFFFFFF


# hashes together a seed with any amount of arguments
def recursive_hash(seed: int, *args: int):
    for arg in args:
        seed = sq_hash(seed, arg)

    return seed


# hashes a string based on a seed
def hash_string(seed, string: str) -> int:
    return recursive_hash(seed, *(ord(letter) for letter in string))
