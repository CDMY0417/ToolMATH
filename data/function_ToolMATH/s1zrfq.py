def solve_linear_equations_i(equation1: tuple[float, float, float], equation2: tuple[float, float, float]):
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1
    if D == 0:
        if Dx == 0 and Dy == 0:
            return 'Infinite solutions'
        else:
            return 'No solution'
    x = Dx / D
    y = Dy / D
    return x, y
