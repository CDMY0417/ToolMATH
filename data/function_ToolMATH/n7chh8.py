def count_integers_in_strict_open_interval(low: float, high: float) -> int:
    return max(0, int(high) - int(low) - 1)
