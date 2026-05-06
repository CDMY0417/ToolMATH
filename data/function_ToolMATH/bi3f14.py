def log_sum_to_product(log_values: list[float], base: int):
    from math import prod
    return prod(base ** x for x in log_values)
