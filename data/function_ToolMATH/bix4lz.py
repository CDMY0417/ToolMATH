def is_perfect_cube_a(n: int) -> bool:
    root = round(n ** (1/3))
    return root ** 3 == n
