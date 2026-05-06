def factor_pairs_h(number: int):
    factors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors
