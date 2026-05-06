import math


def greatest_common_divisor_ae(numbers: list[int]) -> int:
    if not numbers:
        return 0
    return math.gcd(*numbers)
