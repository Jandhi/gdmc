from gdpc.vector_tools import ivec2
from ...structures.legacy_directions import cardinal, get_ivec2


def find_edges(points: set[ivec2]) -> set[ivec2]:
    return {
        point
        for point in points
        if any((point + get_ivec2(direction)) not in points for direction in cardinal)
    }


# Returns outer and inner points of a set of points, where the outer points are determined by some given distance to the edge
def find_outer_and_inner_points(
    points: set[ivec2], distance: int
) -> tuple[set[ivec2], set[ivec2]]:
    edges: set(ivec2) = find_edges(points)
    queue: list[tuple[ivec2, int]] = [(edge, 0) for edge in edges]
    visited = edges.copy()

    while queue:
        point, edge_distance = queue.pop(0)

        if edge_distance >= distance:
            continue

        for direction in cardinal:
            neighbour = point + get_ivec2(direction)

            if neighbour not in points:
                continue

            if neighbour in visited:
                continue

            visited.add(neighbour)

            queue.append((neighbour, edge_distance + 1))
            edges.add(neighbour)

    return edges, (points - edges)
