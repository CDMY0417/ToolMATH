def solve_linear_system_p(A: list[list[float]], B: list[float]) -> list[float]:
    import numpy as np
    A = np.array(A)
    B = np.array(B)
    return np.linalg.solve(A, B).tolist()
