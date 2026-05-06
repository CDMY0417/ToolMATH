def smallest_n_for_integer_sum(factor: int, power_base: int, n_exponent: int):
    required_factors = factor
    current_factor_count = power_base ** (n_exponent - 1)
    n = 1
    while (n * current_factor_count) % required_factors != 0:
        n += 1
    return n
