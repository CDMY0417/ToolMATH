def multiply_polynomials(p1: tuple, p2: tuple):
    a, b, c = p1
    d, e, f = p2
    return (
        a*d,            # x^4 term
        a*e + b*d,      # x^3 term
        a*f + b*e + c*d, # x^2 term
        b*f + c*e,      # x term
        c*f             # constant term
    )
