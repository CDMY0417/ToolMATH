def weighted_sum(values: list[int], frequencies: list[int]) -> int:
    return sum(value * frequency for value, frequency in zip(values, frequencies))
