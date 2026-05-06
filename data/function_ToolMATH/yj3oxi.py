def compute_lcm_c(numbers: list[int]) -> int:
    from math import gcd
    def lcm(a, b):
        return a * b // gcd(a, b)
    result = 1
    for number in numbers:
        result = lcm(result, number)
    return result
