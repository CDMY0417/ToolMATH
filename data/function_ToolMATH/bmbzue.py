def apply_am_gm_inequality_b(variables: list[float]) -> float:
    n = len(variables)
    return n * (sum(variables) / n) ** (1/n)
