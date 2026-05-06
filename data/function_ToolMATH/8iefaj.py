def smallest_divisible_by_factors(factors: list[int]) -> int:
    from math import gcd
    def lcm(a: int, b: int) -> int:
        return abs(a * b) // gcd(a, b)
    lcm_value = factors[0]
    for factor in factors[1:]:
        lcm_value = lcm(lcm_value, factor)
    return lcm_value
