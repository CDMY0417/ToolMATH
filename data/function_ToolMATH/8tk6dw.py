def proper_factors(n: int) -> set:
    factors = set()
    for i in range(1, n):
        if n % i == 0:
            factors.add(i)
    return factors
