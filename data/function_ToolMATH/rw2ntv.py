def least_common_multiple_x(numbers: list[int]) -> int:
    from math import gcd
    def lcm(a, b):
        return a * b // gcd(a, b)
    lcm_value = numbers[0]
    for number in numbers[1:]:
        lcm_value = lcm(lcm_value, number)
    return lcm_value
