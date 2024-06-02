from .hash import sq_hash, hash_string
from .seed import Seed


# deterministic random number generator with state
class RNG(Seed):
    # string_seed allows for a generator to easily be created from some world seed and unique name
    # e.g. RNG(world_seed, 'streets') will generate entirely different from RNG(world_seed, 'districts')
    def __init__(self, seed, string_seed=None) -> None:
        self.seed = seed
        self.state = 0

        if string_seed is not None:
            self.seed = hash_string(seed, string_seed)

    def next(self) -> int:
        val = sq_hash(self.seed, self.state)
        self.state += 1
        return val

    def value(self) -> int:
        return self.next()
