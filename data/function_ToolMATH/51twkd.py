def pair_factors(n: int):
    factors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            factors.append((i, n // i))
            factors.append((-i, -n // i))
    return factors
