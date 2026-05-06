def is_perfect_cube_b(number: int) -> bool:
    root = round(number ** (1/3))
    return root ** 3 == number
