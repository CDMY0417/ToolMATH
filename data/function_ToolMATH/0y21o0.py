def complete_the_square(a: int, b: int, c: int):
    if a == 0:
        return c  # Linear case
    h = b / (2 * a)
    k = (4 * a * c - b * b) / (4 * a)
    return (-(a), h, k)
