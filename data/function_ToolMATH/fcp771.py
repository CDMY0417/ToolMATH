def scale_fraction_to_denominator(numerator: int, denominator: int, target_denominator: int) -> tuple:
    scale_factor = target_denominator // denominator
    return numerator * scale_factor, target_denominator
