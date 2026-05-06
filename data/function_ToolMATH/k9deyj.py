def sum_of_factor_powers(p: int, exp: int):
    return sum(p**i for i in range(exp + 1))
