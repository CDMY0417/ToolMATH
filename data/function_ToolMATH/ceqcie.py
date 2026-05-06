def integer_factors_b(n: int) -> list:
    factors = set()
    for i in range(1, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(-i)
            factors.add(n // i)
            factors.add(-(n // i))
    return sorted(factors)
