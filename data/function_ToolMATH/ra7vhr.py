def square_numbers_in_interval(lo: int, hi: int) -> list:
    squares = []
    start = int(lo**0.5) + 1
    end = int(hi**0.5) + 1
    for i in range(start, end):
        square = i * i
        if lo < square <= hi:
            squares.append(square)
    return squares
