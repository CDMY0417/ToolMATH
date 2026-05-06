def least_value_for_perfect_cube(factorization: dict[int, int]) -> dict[int, int]:
    factor_addition = {}
    for prime, exp in factorization.items():
        if exp % 3 != 0:
            factor_addition[prime] = 3 - (exp % 3)
    return factor_addition
