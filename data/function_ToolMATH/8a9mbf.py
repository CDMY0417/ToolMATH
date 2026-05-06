def integer_solutions_in_quadratic_interval(upper_limit: int):
    solutions = []
    for y in range(-upper_limit, upper_limit + 1):
        if 1 < y**2 < upper_limit:
            solutions.append(y)
    return solutions
