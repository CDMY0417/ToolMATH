def least_common_multiple_ap(numbers: list[int]) -> int:
    from math import gcd
    lcm = 1
    for number in numbers:
        lcm = lcm * number // gcd(lcm, number)
    return lcm
