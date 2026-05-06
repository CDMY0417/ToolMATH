def proper_factors_a(n: int) -> list[int]:
    proper_factors = [i for i in range(2, n) if n % i == 0]
    return proper_factors
