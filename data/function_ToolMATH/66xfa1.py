def factor_expression_b(expression: list[int]):
    from math import gcd
    factor = abs(expression[0])
    for num in expression:
        factor = gcd(factor, abs(num))
    simplified_expression = [num // factor for num in expression]
    return factor, simplified_expression
