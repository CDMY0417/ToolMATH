def permutation_count_a(block_sizes: list[int]) -> int:
    from math import factorial
    arrangements = 1
    for size in block_sizes:
        arrangements *= factorial(size)
    arrangements *= factorial(len(block_sizes))
    return arrangements
