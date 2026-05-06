def least_common_multiple_j(numbers: list[int]) -> int:
    from math import gcd
    def lcm(x, y):
        return x * y // gcd(x, y)
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm(result, number)
    return result
