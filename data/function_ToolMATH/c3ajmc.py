def valid_y_values_less_than(limit: int) -> int:
    count = 0
    n = 1
    while (n**2 + 1) < limit:
        count += 1
        n += 1
    return count
