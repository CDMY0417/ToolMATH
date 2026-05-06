def line_from_point_normal_2d(a: float, b: float, x0: float, y0: float):
    # Line with normal (a,b) through (x0,y0) -> a(x-x0)+b(y-y0)=0
    if b == 0:
        raise ValueError('vertical line: slope undefined')
    m = -a / b
    b0 = (a*x0 + b*y0) / b
    return [m, b0]
