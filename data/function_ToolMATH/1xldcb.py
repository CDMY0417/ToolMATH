def least_common_multiple_b(numbers: list[int]) -> int:
    from math import gcd
    def lcm(x, y):
        return x * y // gcd(x, y)
    lcm_value = numbers[0]
    for number in numbers[1:]:
        lcm_value = lcm(lcm_value, number)
    return lcm_value
