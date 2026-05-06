def solve_piecewise_linear_for_values(y_list, m1: float, b1: float, m2: float, b2: float):
    """Return list of solutions for all y in y_list."""
    out=[]
    for y in y_list:
        if m1 != 0:
            x1=(y-b1)/m1
            if x1 <= 0:
                out.append(x1)
        if m2 != 0:
            x2=(y-b2)/m2
            if x2 > 0:
                out.append(x2)
    return out
