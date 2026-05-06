def factor_count(factors: dict[int, int]) -> int:
    count = 1
    for exponent in factors.values():
        count *= (exponent + 1)
    return count
