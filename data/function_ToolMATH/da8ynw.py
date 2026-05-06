def least_common_multiple_m(numbers: list[int]) -> int:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return a * b // gcd(a, b)
    from functools import reduce
    return reduce(lcm, numbers)
