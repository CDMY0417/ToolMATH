def check_real_solutions(a: int, b: int, c: int) -> bool:
    discriminant = b**2 - 4*a*c
    return discriminant >= 0
