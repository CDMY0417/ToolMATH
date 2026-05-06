def total_combinations_c(choices_per_category: list[int]) -> int:
    from functools import reduce
    from operator import mul
    total = reduce(mul, choices_per_category, 1)
    return total
