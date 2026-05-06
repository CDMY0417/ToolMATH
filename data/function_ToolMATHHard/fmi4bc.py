def sum_partial_fraction_coeffs_shift4(numerator_coeffs):
    # For N(x)/(x+2)^4 = a + b/(x+2) + c/(x+2)^2 + d/(x+2)^3 + e/(x+2)^4
    x = -1
    total = 0
    for i,c in enumerate(numerator_coeffs):
        total += c*(x**i)
    denom = (x+2)**4
    return total/denom
