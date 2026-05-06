def adjust_fraction_to_common_denominator(numerator: int, denominator: int, common_denominator: int) -> int:
    factor = common_denominator // denominator
    return numerator * factor
