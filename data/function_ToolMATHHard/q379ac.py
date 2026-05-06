def sum_coeffs_of_shifted_poly(coeffs, shift: float):
    # Sum of coefficients of g(x)=f(x-shift) equals g(1)=f(1-shift)
    x = 1 - shift
    total = 0
    for i, c in enumerate(coeffs):
        total += c*(x**i)
    return total
