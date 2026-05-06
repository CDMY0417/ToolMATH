def factor_expression_a(coefficients: list[int]) -> tuple:
    from math import gcd
    gcf = abs(coefficients[0])
    for coef in coefficients[1:]:
        gcf = gcd(gcf, abs(coef))
    factored_terms = [coef // gcf for coef in coefficients]
    return gcf, factored_terms
