def sum_of_divisor_powers(base: int, exponent: int):
    return sum(base ** i for i in range(exponent + 1))
