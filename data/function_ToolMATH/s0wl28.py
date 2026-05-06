def square_range(lo: int, hi: int):
    min_square = min(lo**2, hi**2)
    max_square = max(abs(lo), abs(hi))**2
    return (min_square, max_square)
