def convert_to_common_denominator_a(numerator: int, denominator: int, common_denom: int) -> int:
    return numerator * (common_denom // denominator)
