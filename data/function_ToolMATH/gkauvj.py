def compute_greatest_integer_satisfying_inequality(limit: int) -> int:
    x = 1
    while x * x < limit:
        x += 1
    return x - 1
