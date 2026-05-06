def nth_roots_of_unity(n: int) -> list:
    return [k * 360 / n for k in range(n)]
