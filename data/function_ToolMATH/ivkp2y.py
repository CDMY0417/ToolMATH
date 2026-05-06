def nearest_perfect_squares(n: int) -> tuple:
    lower = int(n**0.5)
    upper = lower + 1
    return (lower**2, upper**2)
