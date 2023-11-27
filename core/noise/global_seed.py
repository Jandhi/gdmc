import random


class GlobalSeed:
    seed: int = 0xC00CC1E5

    @staticmethod
    def set(val: int):
        GlobalSeed.seed = val

    @staticmethod
    def get() -> int:
        return GlobalSeed.seed

    @staticmethod
    def randomize():
        GlobalSeed.set(random.randint(0, 1_000_000_000))