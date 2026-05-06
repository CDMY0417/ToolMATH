def count_divisors_l(factors: dict) -> int:
    count = 1
    for _, exponent in factors.items():
        count *= (exponent + 1)
    return count
