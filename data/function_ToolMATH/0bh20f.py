def count_divisors_m(factor_counts: dict) -> int:
    count = 1
    for exponent in factor_counts.values():
        count *= (exponent + 1)
    return count
