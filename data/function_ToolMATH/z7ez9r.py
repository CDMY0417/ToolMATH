def shift_parabola(a: int, b: int, c: int, shift: int):
    new_b = b - 2 * a * shift
    new_c = c + (a * shift ** 2) - (b * shift)
    return (a, new_b, new_c)
