def circle_boundary_y_constraints(x: int, radius: int):
    max_y = int((radius**2 - x**2)**0.5)
    return -max_y, max_y
