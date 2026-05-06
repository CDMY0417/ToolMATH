def is_perfect_cube(n: int) -> bool:
    return round(n ** (1/3)) ** 3 == n
