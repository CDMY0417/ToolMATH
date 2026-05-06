def equation_type(a: float, b: float, c: float):
    if a == b == 0:
        return 'empty'
    elif a == 0 or b == 0:
        if c == 0:
            return 'two lines' if a != b else 'line'
        return 'parabola'
    elif a == b:
        return 'circle' if c > 0 else 'point'
    elif a * b > 0:
        return 'ellipse'
    else:
        return 'hyperbola'
