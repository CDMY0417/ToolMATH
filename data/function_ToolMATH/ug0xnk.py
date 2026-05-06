def least_common_multiple_ai(numbers: list[int]) -> int:
    from math import gcd
    def lcm(a, b):
        return abs(a*b) // gcd(a, b)
    lcm_result = 1
    for number in numbers:
        lcm_result = lcm(lcm_result, number)
    return lcm_result
