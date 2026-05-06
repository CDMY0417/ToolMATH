def count_values_of_a(min_value: int, max_value: int):
    a = 1
    count = 0
    while a * (a + 1) <= max_value:
        if a * (a + 1) >= min_value:
            count += 1
        a += 1
    return count
