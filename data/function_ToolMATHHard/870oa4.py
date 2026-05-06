def sum_xyz_from_two_equations(eq1, eq2):
    # eq = (a,b,c,d) for ax+by+cz=d, if a+b+c equal across, return sum
    a1,b1,c1,d1 = eq1
    a2,b2,c2,d2 = eq2
    A = a1 + a2
    B = b1 + b2
    C = c1 + c2
    if A != B or B != C:
        raise ValueError('coefficients do not match for sum')
    return (d1 + d2) / A
