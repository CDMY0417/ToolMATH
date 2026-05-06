def is_terminating_decimal(n: int, d: int) -> bool:
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    return d == 1
