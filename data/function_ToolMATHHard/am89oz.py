def solve_piecewise_linear_for_value(y: float, m1: float, b1: float, m2: float, b2: float):
    """Return list of x solutions to f(x)=y for a breakpoint at 0."""
    sols=[]
    if m1 != 0:
        x1=(y-b1)/m1
        if x1 <= 0:
            sols.append(x1)
    if m2 != 0:
        x2=(y-b2)/m2
        if x2 > 0:
            sols.append(x2)
    return sols
