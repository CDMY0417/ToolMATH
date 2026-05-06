def simplify_fraction_by_divisor(numerator: int, denominator: int, divisor: int) -> str:
    simplified_numerator = numerator // divisor
    return f'{simplified_numerator}/{denominator}'
