def median_of_even_sorted_list(values: list[int]) -> float:
    mid_index = len(values) // 2
    return (values[mid_index - 1] + values[mid_index]) / 2
