def reflect_through_origin(r: float, theta: float):
    return -r, (theta + 3.141592653589793) % (2 * 3.141592653589793)
