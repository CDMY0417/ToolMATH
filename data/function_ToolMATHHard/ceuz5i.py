def conic_type_from_equation(A: float, B: float, C: float):
    # Classify Ax^2 + By^2 + C = 0
    if A>0 and B>0 and C<0:
        return 'C'
    return 'N'
