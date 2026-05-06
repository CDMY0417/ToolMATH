def solve_absolute_value_equation_a(a: int, b: int, c: int) -> list[float]:
    solutions = []
    if c < 0:
        return solutions
    solutions.append((-b + c) / a)
    solutions.append((-b - c) / a)
    return solutions
