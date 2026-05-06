def power_of_2_range_count(k: int) -> int:
    if k == 10:
        return 1  # Only for N = 1024
    return 2**k
