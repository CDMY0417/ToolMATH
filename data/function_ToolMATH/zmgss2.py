def is_multiple_of_pi(value: float) -> bool:
    import math
    return math.isclose(value % math.pi, 0, abs_tol=1e-9)
