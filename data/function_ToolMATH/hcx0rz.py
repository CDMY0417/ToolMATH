def complete_the_square_n(a: int, b: int, c: int):
    h = b / (2*a)
    k = (b**2) / (4*a)
    corrected_c = c - k
    return (a, h, k, corrected_c)
