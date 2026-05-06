def perfect_squares_in_interval_a(lower_bound: int, upper_bound: int):
    count = 0
    current = 1
    while current**2 <= upper_bound:
        if current**2 > lower_bound:
            count += 1
        current += 1
    return count
