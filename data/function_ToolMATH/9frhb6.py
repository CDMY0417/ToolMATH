def common_denominator(denominators: list[int]) -> int:
    from math import lcm
    return lcm(*denominators)
