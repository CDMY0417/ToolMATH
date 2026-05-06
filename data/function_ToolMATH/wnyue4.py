def sum_of_series(c_values: list[int]) -> int:
    return sum(i * c for i, c in enumerate(c_values, start=1))
