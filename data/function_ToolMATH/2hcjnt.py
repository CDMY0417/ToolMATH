def count_color_groupings(elements: list[int], target_sum: int) -> int:
    from itertools import combinations
    count = 0
    for r in range(1, len(elements)+1):
        for grouping in combinations(elements, r):
            if sum(grouping) == target_sum:
                count += 1
    return count
