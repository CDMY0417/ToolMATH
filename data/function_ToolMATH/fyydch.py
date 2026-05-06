def integer_factors(n: int):
    factors = set()
    for i in range(1, int(abs(n)**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
            factors.add(-i)
            factors.add(-n // i)
    return list(factors)
