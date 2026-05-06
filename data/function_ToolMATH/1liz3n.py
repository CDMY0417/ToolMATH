def roots_of_unity_a(n: int, r: float):
    from cmath import rect, pi
    return [rect(r ** (1/n), 2 * pi * k / n) for k in range(n)]
