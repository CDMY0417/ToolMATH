def calculate_other_endpoint_coordinates_sum(endpoint: tuple, midpoint: tuple) -> float:
    x1, y1 = endpoint
    mx, my = midpoint
    other_x = 2 * mx - x1
    other_y = 2 * my - y1
    return other_x + other_y
