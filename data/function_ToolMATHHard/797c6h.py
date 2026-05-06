def coeffs_from_double_root(x0: float):
    # For f(x)=x^3+bx+c with (x-x0)^2 factor, b=-3x0^2, c=2x0^3
    b = -3*(x0**2)
    c = 2*(x0**3)
    return [b, c]
