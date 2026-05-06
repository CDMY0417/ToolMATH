def solve_linear_system_g(A: list[list[float]], b: list[float]) -> list[float]:
    import numpy as np
    A = np.array(A)
    b = np.array(b)
    solution = np.linalg.solve(A, b)
    return solution.tolist()
