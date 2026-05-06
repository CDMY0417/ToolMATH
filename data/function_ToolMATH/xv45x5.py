def complex_number_coordinates(x_squared: int, y_squared: int):
    import math
    x = int(math.sqrt(x_squared))
    y = int(math.sqrt(y_squared))
    return [(x, y), (x, -y), (-x, y), (-x, -y)]
