def add_polynomials_b(p1: list[float], p2: list[float]) -> list[float]:
    length = max(len(p1), len(p2))
    result = [0] * length
    for i in range(len(p1)):
        result[i] = p1[i]
    for i in range(len(p2)):
        result[i] += p2[i]
    return result
