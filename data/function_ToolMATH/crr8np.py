def simplify_fraction_ay(numerator_coeff: int, numerator_power: int, denominator_coeff: int, denominator_power: int):
    simplified_coeff = numerator_coeff / denominator_coeff
    simplified_power = numerator_power - denominator_power
    return simplified_coeff, simplified_power
