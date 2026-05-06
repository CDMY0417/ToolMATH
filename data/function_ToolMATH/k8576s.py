def verify_solution_matches(x: float, k: int):
    return abs(x ** 3 - 1 - k) < 1e-9
