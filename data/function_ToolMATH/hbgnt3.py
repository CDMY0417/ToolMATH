def integers_in_interval(low: float, high: float):
    low_int = int(low) + 1 if low % 1 != 0 else int(low)
    high_int = int(high) - 1 if high % 1 != 0 else int(high) - 1
    return list(range(low_int, high_int + 1))
