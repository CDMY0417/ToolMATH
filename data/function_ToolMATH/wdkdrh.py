from math import gcd

def factor_out_gcd_c(coefficients: list[int]):
    common_gcd = abs(coefficients[0])
    for coeff in coefficients[1:]:
        common_gcd = gcd(common_gcd, abs(coeff))

    if common_gcd == 1:
        return coefficients, 1

    return [coeff // common_gcd for coeff in coefficients], common_gcd
