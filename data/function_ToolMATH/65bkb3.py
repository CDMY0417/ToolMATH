def complete_the_square_ap(a: int, b: int, c: int):
    b_new = b / (2 * a)
    c_new = c + (b_new ** 2)
    return b_new, c_new
