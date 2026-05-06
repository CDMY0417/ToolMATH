def polynomial_division(dividend: list[int], divisor: list[int]):
    from sympy import Poly
    dividend_poly = Poly(dividend, domain='QQ')
    divisor_poly = Poly(divisor, domain='QQ')
    quotient, remainder = dividend_poly.div(divisor_poly)
    return quotient.all_coeffs(), remainder.all_coeffs()
