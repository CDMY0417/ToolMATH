def least_common_multiple_a(numbers: list[int]) -> int:
    from math import gcd
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    result = numbers[0]
    for n in numbers[1:]:
        result = lcm(result, n)
    return result
