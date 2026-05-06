def convert_fraction_a(numerator: int, denominator: int, new_denominator: int) -> int:
    return numerator * (new_denominator // denominator)
