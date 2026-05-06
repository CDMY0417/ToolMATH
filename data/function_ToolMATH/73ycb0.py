def roots_of_square_equation(c: float):
    if c < 0:
        return []
    root = c ** 0.5
    return [root, -root]
