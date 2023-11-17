from core.noise.random import *

# Class that wraps the seed value
class Seed:
    def __init__(self, value) -> None:
        self.value = value

    def value(self) -> int:
        return self.value
    
    # random.py functions
    def randint(self, max : int) -> int:
        return randint(self.value(), max)
    
    def randrange(self, min : int, max : int) -> int:
        return randrange(self.value(), min, max)
    
    def choose(self, items : list):
        return choose(self.value(), items)
    
    def pop(self, items : list):
        return pop(self.value(), items)
    
    def choose_weighted(self, items : dict[any, int]):
        return choose_weighted(self.value(), items)

    def pop_weighted(self, items : dict[any, int]):
        return pop_weighted(self.value(), items)
    
    def odds(self, successes : int, failures : int) -> bool:
        return odds(self.value(), successes, failures)

    def chance(self, successes : int, total : int) -> bool:
        return chance(self.value(), successes, total)
    
    def shuffle(self, items : list) -> list:
        return shuffle(self.value(), items)