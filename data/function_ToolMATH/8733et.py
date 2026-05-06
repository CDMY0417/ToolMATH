def find_common_denominator_c(denominators: list[int]) -> int:
    from sympy import lcm
    return lcm(denominators)
