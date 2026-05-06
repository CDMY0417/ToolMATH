def is_perfect_cube_c(n: int) -> bool:
    cube_root = round(n ** (1/3))
    return cube_root ** 3 == n
