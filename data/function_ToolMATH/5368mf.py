def compound_interest_a(P: float, r: float, n: int, t: int) -> float:
    return P * (1 + r / n) ** (n * t)
