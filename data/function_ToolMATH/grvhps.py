def least_common_multiple_list(numbers: list[int]) -> int:
    from functools import reduce
    def lcm(x, y):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        return abs(x * y) // gcd(x, y)
    return reduce(lcm, numbers)
