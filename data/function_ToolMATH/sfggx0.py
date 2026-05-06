def largest_perfect_square_factor(prime_factors: dict[int, int]) -> int:
    product = 1
    for prime, exp in prime_factors.items():
        product *= prime ** (exp // 2)
    return product ** 2
