def complete_square_ab(a: int, b: int, c: int):
    m = b / (2*a)
    completed_square = f'{a}(x - {m})^2'
    constant_adjustment = c - a * m**2
    return completed_square, constant_adjustment
