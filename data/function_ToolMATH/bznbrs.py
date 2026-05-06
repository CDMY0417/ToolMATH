def solve_two_equations(equation1: tuple[float, float, float], equation2: tuple[float, float, float]) -> tuple[float, float]:
    (a1, b1, c1) = equation1
    (a2, b2, c2) = equation2

    b2_new = b2 * a1
    a2_new = a2 * a1
    c2_new = c2 * a1

    a1_new = a1 * a2
    b1_new = b1 * a2
    c1_new = c1 * a2

    variable2 = (c2_new - c1_new) / (b2_new - b1_new)
    variable1 = (c1 - b1 * variable2) / a1

    return variable1, variable2
