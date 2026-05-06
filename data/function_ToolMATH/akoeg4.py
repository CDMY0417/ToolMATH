def least_common_multiple_k(numbers: list[int]) -> int:
    from math import gcd
    def lcm(x, y):
        return x * y // gcd(x, y)
    result = 1
    for number in numbers:
        result = lcm(result, number)
    return result
