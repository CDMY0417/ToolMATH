def rationalize_denominator_root(numerator: int, denominator: int, root_degree: int):
    multiplier = denominator ** (1 / root_degree)
    new_numerator = numerator * multiplier
    new_denominator = denominator * (multiplier ** (root_degree - 1))
    return new_numerator, new_denominator
