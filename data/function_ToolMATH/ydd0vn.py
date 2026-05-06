def perfect_squares_less_than(n: int):
    squares = []
    i = 1
    while i * i < n:
        squares.append(i * i)
        i += 1
    return squares
