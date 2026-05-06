def count_perfect_square_factors(prime_factors: dict) -> int:
    count = 1
    for exponent in prime_factors.values():
        count *= (exponent // 2) + 1
    return count
