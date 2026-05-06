def solve_two_linear_equations(equation1: tuple[float, float, float], equation2: tuple[float, float, float]) -> tuple[int, int]:
    (a1, b1, c1) = equation1
    (a2, b2, c2) = equation2
    # Using substitution method
    # Express x in terms of y from first equation: a1*x + b1*y = c1 -> x = (c1 - b1*y) / a1
    x_in_terms_of_y = lambda y: (c1 - b1 * y) / a1
    # Substitute in the second equation
    # a2 * ((c1 - b1 * y) / a1) + b2 * y = c2
    # Reorganize to solve for y: a2/a1 * c1 - a2/a1 * b1 * y + b2 * y = c2
    # Let k = a2/a1 * b1 - b2, rearrange to: y = (a2/a1 * c1 - c2) / k
    k = (a2 * b1 / a1) - b2
    y = (a2 / a1 * c1 - c2) / k
    x = x_in_terms_of_y(y)
    return int(x), int(y)
