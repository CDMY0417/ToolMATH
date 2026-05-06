def to_common_denominator(numerator: int, denominator: int, common_denominator: int):
    multiplier = common_denominator // denominator
    return (numerator * multiplier, common_denominator)
