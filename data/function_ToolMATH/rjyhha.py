def find_smallest_perfect_cube_greater_than(number: int) -> int:
    import math
    return math.ceil(number ** (1/3)) ** 3
