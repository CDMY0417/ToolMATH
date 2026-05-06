def simplify_radical_expression(a: int, x: int) -> (int, int):
    from math import isqrt
    for i in range(isqrt(x), 0, -1):
        if x % (i * i) == 0:
            return a * i, x // (i * i)
    return a, x
