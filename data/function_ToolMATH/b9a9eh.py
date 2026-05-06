def factor_expression(term1: tuple, term2: tuple, gcf: tuple):
    coeff1, power1 = term1
    coeff2, power2 = term2
    gcd_coeff, gcd_power = gcf
    factored_term1 = (coeff1 // gcd_coeff, power1 - gcd_power)
    factored_term2 = (coeff2 // gcd_coeff, power2 - gcd_power)
    return ((gcd_coeff, gcd_power), [factored_term1, factored_term2])
