def sum_of_squares_sin(n: int):
    import math
    return sum(math.sin(math.radians(i))**2 for i in range(n + 1))
