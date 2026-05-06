def binomial_term(r: float, x: float, y: float, k: int):
    from math import factorial
    if k == 0:
        return x ** r
    coefficient = 1
    for i in range(k):
        coefficient *= (r - i) / (i + 1)
    return coefficient * (x ** (r - k)) * (y ** k)
