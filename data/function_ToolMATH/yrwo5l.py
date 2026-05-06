def piecewise_function(x: int):
    if x > 5:
        return x**2 + 1
    elif -5 <= x <= 5:
        return 2 * x - 3
    else:
        return 3
