def solve_linear_system_d(coefficients: list[list[float]], constants: list[float]) -> list[float]:
    from numpy.linalg import solve
    return solve(coefficients, constants).tolist()
