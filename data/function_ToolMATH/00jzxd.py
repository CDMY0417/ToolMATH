def multiply_polynomials_c(p1: list[float], p2: list[float]) -> list[float]:
    result = [0] * (len(p1) + len(p2) - 1)
    for i, a in enumerate(p1):
        for j, b in enumerate(p2):
            result[i + j] += a * b
    return result
