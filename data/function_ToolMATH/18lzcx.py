def simplify_square_root(n: int) -> tuple[int, int]:
    factor = 1
    while n % (factor * factor) == 0:
        factor += 1
    factor -= 1
    return factor, n // (factor * factor)
