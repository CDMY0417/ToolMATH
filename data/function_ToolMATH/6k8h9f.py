def midpoint_to_endpoint(midpoint: tuple, endpoint: tuple) -> tuple:
    mx, my = midpoint
    ex, ey = endpoint
    x = 2 * mx - ex
    y = 2 * my - ey
    return (x, y)
