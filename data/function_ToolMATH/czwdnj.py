def count_combinations_d(group_sizes: list[int]) -> int:
    from functools import reduce
    from operator import mul
    return reduce(mul, group_sizes, 1)
