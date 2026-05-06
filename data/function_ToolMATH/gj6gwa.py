def equation_of_circle_from_center_radius(center_x: float, center_y: float, radius: float):
    D = -2 * center_x
    E = -2 * center_y
    F = center_x**2 + center_y**2 - radius**2
    return 1, 1, D, E, F
