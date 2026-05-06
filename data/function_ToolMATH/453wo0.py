def ways_for_larger_number(target: int) -> int:
    if target < 1 or target > 6:
        return 0
    ways = 1 + 2 * (target - 1)
    return ways
