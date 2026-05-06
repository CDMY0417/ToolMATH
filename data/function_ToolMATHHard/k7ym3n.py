def tan_sum_from_tan_and_cot_sums(tan_sum: float, cot_sum: float):
    prod = tan_sum / cot_sum
    return tan_sum / (1 - prod)
