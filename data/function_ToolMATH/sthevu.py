def integer_trio_sum(total: int, min_value: int):
    for a in range(min_value, total - 2 * min_value + 1):
        for b in range(a, total - a - min_value + 1):
            c = total - a - b
            if c >= b:
                yield a, b, c
