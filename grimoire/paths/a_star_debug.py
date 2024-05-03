from heapq import heappop, heappush
from gdpc import Editor, Block
from ..core.utils.vectors import y_ivec3
from ..paths.a_star import COUNTER_LIMIT, COUNTER_LIMIT_EXCEEDED

# get_neighbours takes state
# get_cost takes prev_cost and path


def a_star_debug(start, end, get_neighbours, get_cost, editor: Editor) -> list:
    first_path = [start]
    paths = [(get_cost(0, first_path), first_path)]
    visited = set()
    counter = 0

    while paths:
        counter += 1
        if counter % 10000 == 0:
            print(f"counter at {counter}")

        if counter > COUNTER_LIMIT:
            return COUNTER_LIMIT_EXCEEDED

        curr_cost, curr_path = heappop(paths)

        endpoint = curr_path[-1]

        visited.add(endpoint)
        editor.placeBlock(endpoint + y_ivec3(20), Block("blue_wool"))

        for neighbour in get_neighbours(endpoint):
            if neighbour in visited:
                continue

            if neighbour == end:
                return curr_path + [neighbour]

            new_path = curr_path + [neighbour]
            cost = get_cost(curr_cost, new_path)

            heappush(paths, (cost, new_path))

    # no dice
    return None
