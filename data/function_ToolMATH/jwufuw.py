def largest_common_power(base: int, exp1: int, exp2: int) -> int:
    return base ** min(exp1, exp2)
