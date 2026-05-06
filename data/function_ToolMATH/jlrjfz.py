def convert_to_common_denominator(a_num: int, a_denom: int, b_num: int, b_denom: int) -> tuple:
    common_denom = a_denom * b_denom
    new_a_num = a_num * b_denom
    new_b_num = b_num * a_denom
    return (new_a_num, new_b_num, common_denom)
