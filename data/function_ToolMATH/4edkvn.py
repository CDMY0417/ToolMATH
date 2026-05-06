def least_common_multiple_d(numbers: list[int]) -> int:
    from math import gcd
    lcm = 1
    for number in numbers:
        lcm = abs(lcm * number) // gcd(lcm, number)
    return lcm
