def perfect_squares_in_range_a(min_value: int, max_value: int):
    squares = []
    n = 1
    while n * n <= max_value:
        if n * n >= min_value:
            squares.append(n * n)
        n += 1
    return squares
