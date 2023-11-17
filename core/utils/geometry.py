from gdpc.vector_tools import ivec2
from gdpc import WorldSlice
from core.structures.legacy_directions import cardinal, get_ivec2

#finds the neighbours points of a point in a set
def get_neighbours_in_set(point : ivec2, set : list[ivec2]) -> list[ivec2]:
    neighbours = []
    
    for direction in cardinal:
        delta = get_ivec2(direction)
        neighbour = point + delta

        if neighbour in set:
            neighbours.append(neighbour)

    return neighbours

#finds the neighbours points of a point not in a set
def get_neighbours_not_in_set(point : ivec2, set : list[ivec2]) -> list[ivec2]:
    neighbours = []
    
    for direction in cardinal:
        delta = get_ivec2(direction)
        neighbour = point + delta

        if neighbour not in set:
            neighbours.append(neighbour)

    return neighbours

#returns the subset of points which are edge points, returns both a list and dict
def get_outer_points(points : list[ivec2], world_slice : WorldSlice): # -> list[ivec2], dict:
    outer_points: list[ivec2] = []
    outer_points_dict: dict() = {}

    for point in points:
        if len(get_neighbours_in_set(point, points)) != 4:
            outer_points.append(point)
            outer_points_dict[point] = True
        
    return outer_points, outer_points_dict


#returns true if the line formed by the two points is 'straight' (on the minecraft plane)
def is_straight_ivec2(previous : ivec2, next : ivec2, length : int):
    vec_line = previous - next
    if (abs(vec_line.x) == length and vec_line.y == 0) or (abs(vec_line.y) == length and vec_line.x == 0) or (abs(vec_line.x) == length and abs(vec_line.x) == abs(vec_line.y)):
        return True
    return False


#returns true if the line formed by the two points is 'straight' (on the minecraft plane)
def is_straight_not_diagonal_ivec2(previous : ivec2, next : ivec2, length : int):
    vec_line = previous - next
    if (abs(vec_line.x) == length and vec_line.y == 0) or (abs(vec_line.y) == length and vec_line.x == 0):
        return True
    return False

#returns true if all of points neighbours (including diagonal) are in dict
def is_point_surrounded_dict(point : ivec2, dict):
    neighbours = [ivec2(x, z) for x in range(point.x -1, point.x + 2) for z in range(point.y -1, point.y + 2)]
    for neighbour in neighbours:
        if dict.get(neighbour) == None:
            return False
    return True 