from gdpc.vector_tools import ivec2, distance2

from ...structures.legacy_directions import cardinal, get_ivec2, left, right


def midpoint(points: set[ivec2]) -> ivec2:
    return sum(points) / len(points)


def calculate_stretch(points: set[ivec2]) -> ivec2:
    stretch = ivec2(1, 1)
    mid = midpoint(points)

    for point in points:
        stretch += abs(mid - point)

    return stretch


def voronoi_split(
    points: set[ivec2], point_a: ivec2, point_b: ivec2
) -> tuple[set[ivec2], set[ivec2]]:
    set_a = set()
    set_b = set()

    for point in points:
        if distance2(point, point_a) < distance2(point, point_b):
            set_a.add(point)
        else:
            set_b.add(point)

    return set_a, set_b


def split(points: set[ivec2]) -> tuple[set[ivec2], set[ivec2]]:
    mid = midpoint(points)

    best_split = None

    # You want this low like golf
    def split_score(split):
        evenness = abs(len(split[0]) - len(split[1]))

        # maybe add stretch as goal
        stretch_a = calculate_stretch(split[0])
        stretch_b = calculate_stretch(split[1])

        stretch_penalty_a = max(stretch_a.x, stretch_a.y) / min(
            stretch_a.x, stretch_a.y
        )
        stretch_penalty_b = max(stretch_b.x, stretch_b.y) / min(
            stretch_b.x, stretch_b.y
        )

        return evenness + stretch_penalty_a * 0.1 + stretch_penalty_b * 0.1

    for point_a, point_b in [
        (ivec2(1, 0), ivec2(-1, 0)),
        (ivec2(0, 1), ivec2(0, -1)),
    ]:
        split = voronoi_split(points, mid + point_a, mid + point_b)

        if best_split is None:
            best_split = split
            continue

        if split_score(split) < split_score(best_split):
            best_split = split

    return best_split


def find_edges(points: set[ivec2]) -> set[ivec2]:
    edges = set()

    for point in points:
        for direction in cardinal:
            neighbour = point + get_ivec2(direction)

            if neighbour not in points:
                edges.add(point)
                break

    return edges


def find_outer_direction(point: ivec2, points: set[ivec2], first_wins_ties=True) -> str:
    best_dir = None
    best_dir_score = 0

    for direction in cardinal:
        score = 0
        vector = get_ivec2(direction)
        left_vector = get_ivec2(left[direction])
        right_vector = get_ivec2(right[direction])

        for base_vec in (ivec2(0, 0), left_vector, right_vector):
            for dist in range(5):
                pt = point + base_vec + dist * vector

                if pt not in points:
                    score += 1

        if score > best_dir_score or (not first_wins_ties and score == best_dir_score):
            best_dir = direction
            best_dir_score = score

    return best_dir


def find_outline(points: set[ivec2], thickness: int = 1) -> set[ivec2]:
    points = points.copy()
    edges = find_edges(points)
    outline_set = set()

    for _ in range(thickness):
        outline = set()

        for edge in edges:
            for dir in cardinal:
                pt = edge + get_ivec2(dir)

                if pt not in points and pt not in outline_set:
                    outline.add(pt)

        outline_set |= outline
        edges = outline

    return outline_set
