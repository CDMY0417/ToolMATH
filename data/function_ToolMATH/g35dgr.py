def count_divisors_g(exponents: list[int]) -> int:
    count = 1
    for e in exponents:
        count *= (e + 1)
    return count
