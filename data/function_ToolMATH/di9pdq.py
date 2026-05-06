def evaluate_piecewise_function(x: int, a: int, b: int, c: int):
    if x > 0:
        return a * x + 3
    elif x == 0:
        return a * b
    else:
        return b * x + c
