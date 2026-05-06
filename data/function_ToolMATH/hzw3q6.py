def perfect_squares_up_to_n(n: int) -> list[int]:
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1
    return squares
