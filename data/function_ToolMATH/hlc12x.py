def find_floor_value_for_target(target: int) -> int:
    for n in range(target):
        if n * n <= target < (n + 1) * (n + 1):
            return n
    return -1  # This should never happen if target is positive.
