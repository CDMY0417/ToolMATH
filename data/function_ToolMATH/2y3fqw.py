def perfect_squares_in_range(start: int, end: int):
    squares = []
    x = 1
    while x**2 <= end:
        if x**2 >= start:
            squares.append(x**2)
        x += 1
    return squares
