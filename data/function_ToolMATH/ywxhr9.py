def count_perfect_squares_in_range_a(low: int, high: int) -> int:
    start = int(low**0.5)
    end = int(high**0.5)
    return end - start + (1 if start**2 >= low else 0)
