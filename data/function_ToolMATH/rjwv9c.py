def count_ways_to_choose(groups: list[int]) -> int:
    total_ways = 1
    for group in groups:
        total_ways *= group
    return total_ways
