def least_common_multiple_p(numbers: list[int]) -> int:
    from functools import reduce
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return a * b // gcd(a, b)
    return reduce(lcm, numbers, 1)
