def sum_of_squares_cos(degrees: int):
    import math
    return sum(math.cos(math.radians(i))**2 for i in range(degrees + 1))
