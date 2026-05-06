def find_perfect_cube_greater_than(num: int) -> int:
    n = 1
    while n**3 <= num:
        n += 1
    return n**3
