def count_combinations_k(choices: list[int]) -> int:
    from functools import reduce
    from operator import mul
    return reduce(mul, choices, 1)
