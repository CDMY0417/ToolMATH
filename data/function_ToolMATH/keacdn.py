def count_possible_sums(n: int, m: int) -> int:
    min_sum = n * 1
    max_sum = n * m
    return max_sum - min_sum + 1
