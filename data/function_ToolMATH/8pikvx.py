def simplify_sqrt_a(factors: dict[str, int]):
    coeff = 1
    remaining_factors = {}
    for factor, power in factors.items():
        pair_power = power // 2
        leftover_power = power % 2
        if factor != 'p':
            coeff *= pow(int(factor), pair_power)
        if leftover_power > 0:
            remaining_factors[factor] = leftover_power
    if 'p' in factors:
        p_power = factors['p'] // 2
        coeff *= pow('p', p_power)
        if factors['p'] % 2 > 0:
            remaining_factors['p'] = 1
    return coeff, remaining_factors
