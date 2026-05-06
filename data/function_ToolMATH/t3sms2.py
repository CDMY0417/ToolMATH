def convert_repeating_decimal_to_fraction_c(repeating_decimal: str):
    from sympy import Rational
    if '(' in repeating_decimal:
        non_repeating, repeating = repeating_decimal.split('(')
        repeating = repeating.rstrip(')')
        non_repeating_len = len(non_repeating.split('.')[1]) if '.' in non_repeating else 0
        repeating_len = len(repeating)
        numerator = int(non_repeating.replace('.', '') + repeating) - int(non_repeating.replace('.', ''))
        denominator = (10**(non_repeating_len + repeating_len) - 10**non_repeating_len)
        return Rational(numerator, denominator)
    else:
        return Rational(float(repeating_decimal))
