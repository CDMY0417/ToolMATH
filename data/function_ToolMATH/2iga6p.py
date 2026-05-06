def solve_x_squared_equals_y(value: int):
    root = int(value**0.5)
    if root**2 == value:
        return -root, root
    return ()
