def lcm_of_list(numbers: list[int]) -> int:
    from functools import reduce
    def lcm(x, y):
        return (x * y) // gcd(x, y)
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return reduce(lcm, numbers, 1)
