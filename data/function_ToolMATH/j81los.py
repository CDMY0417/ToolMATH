def convert_repeating_decimal_to_fraction_b(whole_part: int, non_repeating: str, repeating: str):
    len_non_repeating = len(non_repeating)
    len_repeating = len(repeating)
    if len_non_repeating == 0:
        n = int(repeating)
        d = int('9' * len_repeating)
    else:
        non_rep_dec = int(non_repeating)
        rep_dec = int(repeating)
        n = non_rep_dec * (10**len_repeating - 1) + rep_dec - non_rep_dec
        d = (10**len_non_repeating) * (10**len_repeating - 1)
    fraction = (whole_part * d + n, d)
    from math import gcd
    common_divisor = gcd(fraction[0], fraction[1])
    return (fraction[0] // common_divisor, fraction[1] // common_divisor)
