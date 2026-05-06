def divisor_count_from_exponents(exponents: list[int]) -> int:
    count = 1
    for exponent in exponents:
        count *= (exponent + 1)
    return count
