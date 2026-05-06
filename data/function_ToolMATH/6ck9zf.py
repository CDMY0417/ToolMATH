def next_collatz_value(x: int) -> int:
    if x % 2 == 0:
        return x // 2
    else:
        return 3 * x + 1
