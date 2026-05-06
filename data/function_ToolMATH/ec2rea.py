def digit_factors(n: int):
    factors = [i for i in range(1, 10) if n % i == 0]
    return sorted(factors, reverse=True)
