def least_common_multiple(numbers: list[int]) -> int:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    lcm_value = 1
    for number in numbers:
        lcm_value = lcm(lcm_value, number)
    return lcm_value
