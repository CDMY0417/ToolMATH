def least_common_multiple_y(numbers: list[int]) -> int:
    from math import gcd
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    lcm_value = numbers[0]
    for num in numbers[1:]:
        lcm_value = lcm(lcm_value, num)
    return lcm_value
