def cancel_common_factors(numerator: str, denominator: str, factor: str):
    if factor in numerator and factor in denominator:
        simplified_numerator = numerator.replace(factor, '')
        simplified_denominator = denominator.replace(factor, '')
        return simplified_numerator, simplified_denominator
    return numerator, denominator
