def max_perfect_square_factors(prime_factors: dict[int, int]) -> dict[int, int]:
    square_factors = {}
    for prime, exp in prime_factors.items():
        square_factors[prime] = exp // 2 * 2
    return square_factors
