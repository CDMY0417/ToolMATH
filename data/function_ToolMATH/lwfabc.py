def total_combinations_b(choices: list[int]) -> int:
    from functools import reduce
    from operator import mul
    return reduce(mul, choices, 1)
