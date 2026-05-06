def solve_c_for_polynomial_value(coeffs, x0: float):
    # For f(x)=p(x)+c with constant term c, set f(x0)=0 -> c = -p(x0)
    total = 0
    for i, c in enumerate(coeffs):
        total += c*(x0**i)
    return -total
