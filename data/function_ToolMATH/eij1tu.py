def is_terminating_denominator(k: int) -> bool:
    while k % 2 == 0:
        k //= 2
    while k % 5 == 0:
        k //= 5
    return k == 1
