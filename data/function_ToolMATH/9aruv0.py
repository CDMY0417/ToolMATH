def weighted_sum_a(values: list[int], counts: list[int]) -> int:
    return sum(value * count for value, count in zip(values, counts))
