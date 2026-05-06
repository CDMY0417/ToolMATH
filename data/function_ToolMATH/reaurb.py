def common_denominator_a(a_numerator: int, a_denominator: int, b_numerator: int, b_denominator: int) -> tuple:
    common_den = a_denominator * b_denominator
    a_num_common = a_numerator * b_denominator
    b_num_common = b_numerator * a_denominator
    return (a_num_common, b_num_common, common_den)
