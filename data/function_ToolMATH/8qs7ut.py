def least_common_multiple_g(numbers: list[int]) -> int:
    from functools import reduce
    def lcm(a, b):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        return (a * b) // gcd(a, b)
    return reduce(lambda x, y: lcm(x, y), numbers)
