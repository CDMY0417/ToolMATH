def count_combinations_j(choices: list[int]) -> int:
    from functools import reduce
    from operator import mul
    return reduce(mul, choices)
