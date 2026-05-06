def remainder_from_two_values(x1: float, y1: float, x2: float, y2: float):
    # Compute ax+b that fits (x1,y1),(x2,y2)
    a = (y2 - y1)/(x2 - x1)
    b = y1 - a*x1
    return [a, b]
