def least_common_multiple_o(numbers: list[int]) -> int:
    from math import gcd
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = lcm * num // gcd(lcm, num)
    return lcm
