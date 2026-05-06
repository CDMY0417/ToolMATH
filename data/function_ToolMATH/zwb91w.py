def generate_modular_solutions(a: int, m: int, upper_limit: int):
    x = a
    solutions = []
    while x <= upper_limit:
        if x > 0:
            solutions.append(x)
        x += m
    return solutions
