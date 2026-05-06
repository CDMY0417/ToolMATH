def rewrite_fraction_with_common_denominator(numerator: int, denominator: int, common_denominator: int) -> tuple:
    factor = common_denominator // denominator
    return numerator * factor, common_denominator
