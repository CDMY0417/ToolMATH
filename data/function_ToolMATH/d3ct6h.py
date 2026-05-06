def ackermann_function(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann_function(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann_function(m - 1, ackermann_function(m, n - 1))
