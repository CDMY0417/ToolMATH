def simplify_sqrt(factors: dict) -> tuple[int, int]:
    outside = 1
    inside = 1
    for p, exp in factors.items():
        outside *= p ** (exp // 2)
        if exp % 2 == 1:
            inside *= p
    return outside, inside
