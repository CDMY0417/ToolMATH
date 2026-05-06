def roots_of_quadratic(a: int, b: int, c: int):
    disc = b**2 - 4*a*c
    if disc < 0:
        return None
    elif disc == 0:
        return (-b / (2 * a),)
    else:
        root1 = (-b + disc**0.5) / (2 * a)
        root2 = (-b - disc**0.5) / (2 * a)
        return (root1, root2)
