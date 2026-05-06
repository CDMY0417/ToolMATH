def count_combinations_i(option_counts: list[int]) -> int:
    from functools import reduce
    from operator import mul
    return reduce(mul, option_counts, 1)
