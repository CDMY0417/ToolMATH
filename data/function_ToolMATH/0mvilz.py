def count_even_values_in_range(low: int, high: int) -> int:
    count = 0
    for i in range(low, high + 1):
        if i % 2 == 0:
            count += 1
    return count
