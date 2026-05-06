def solve_absolute_linear_equation(a: int, b: int, c: int):
    solutions = []
    for value in [c, -c]:
        n = (value - b) / a
        solutions.append(n)
    return solutions
