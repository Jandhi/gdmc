from ..districts.district import District

RURAL_SIZE_RATIO = (
    3  # we expect rural districts to be this times larger in area than urban ones
)


# Merges districts until we have a target number reached
def merge_down(
    districts: list[District], district_map: list[list[District]], target_number: int
):
    identities = {
        district: district for district in districts
    }  # tracks whether a districts is truly itself
    district_count = len(districts)

    ignore = set()

    while district_count > target_number:
        child = find_smallest_adjusted_district(districts, ignore)

        if child is None:
            break

        neighbours: list[District] = child.get_adjacent_districts()

        parent = get_best_merge_candidate(child, neighbours)

        if parent is None:
            ignore.add(child)

            if child.area < 10:  # remove garbage districts
                districts.remove(child)
                district_count -= 1
                identities[child] = None

            continue

        merge(parent, child, districts, identities)
        district_count -= 1

    fix_map_and_edges(district_map, districts, identities)


def find_smallest_adjusted_district(
    districts: list[District], ignore: set[District]
) -> District:
    smallest = None
    area = 10000000

    for district in districts:
        if district in ignore:
            continue

        if get_adjusted_area(district) < area:
            smallest = district
            area = district.area

    return smallest


def get_best_merge_candidate(district: District, options: list[District]) -> District:
    best = None
    best_score = -1
    candidate_scores = {}

    for option in options:
        if (
            district.is_urban != option.is_urban
        ):  # don't merge different types of districts!
            continue

        score = get_candidate_score(district, option)
        candidate_scores[option] = score
        if score > best_score:
            best = option
            best_score = score

    output = f"\tConsidering options for {district}: "
    for candidate, score in candidate_scores.items():
        output += f"({candidate}: {score}) "
    print(output)

    return best


def get_candidate_score(district: District, candidate: District) -> float:
    return (
        1000.0
        * district.get_adjacency_ratio(candidate)
        / float(get_adjusted_area(candidate))
    )


def get_adjusted_area(district: District) -> int:
    if district.is_urban:
        return district.area
    else:
        return district.area // RURAL_SIZE_RATIO


# merges child districts into parent
# NOTE: this will create outdated edges (between parent and child).
# Edges should be scanned for again after the merging process.
def merge(
    parent: District,
    child: District,
    districts: list[District],
    identities: dict[District, District],
):
    print(f"\tMerging {child} into {parent}")

    districts.remove(child)
    identities[child] = parent

    parent.area += child.area
    parent.edges |= child.edges  # set addition

    parent.points |= child.points
    parent.points_2d |= child.points_2d

    # merge child's neighborus to parent
    for district, adjacency_count in child.adjacency.items():
        if district == parent:
            continue

        if district not in parent.adjacency:
            parent.adjacency[district] = 0

        parent.adjacency[district] += adjacency_count
        parent.adjacencies_total += adjacency_count

    parent.adjacency.pop(child)

    # switch child for parent in other districts
    for district in districts:
        if district == parent:
            continue

        if child in district.adjacency:
            if parent not in district.adjacency:
                district.adjacency[parent] = 0

            district.adjacency[parent] += district.adjacency[child]
            district.adjacency.pop(child)

    # add alias tracking for districts map
    for alias in list(identities.keys()):
        if identities[alias] == child:
            identities[alias] = parent


def fix_map_and_edges(
    district_map: list[list[District]],
    districts: list[District],
    identities: dict[District, District],
):
    # Fixes map
    for item in district_map:
        for z in range(len(district_map[0])):
            district = item[z]

            if district != None:
                item[z] = identities[district]
