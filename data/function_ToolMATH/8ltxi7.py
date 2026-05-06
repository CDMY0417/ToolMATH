def ways_to_select_one_each(groups: list[int]) -> int:
    ways = 1
    for group in groups:
        ways *= group
    return ways
