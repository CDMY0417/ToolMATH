def subtract_fractions(numer1: int, denom1: int, numer2: int, denom2: int):
    common_denom = denom1 * denom2
    new_numer1 = numer1 * denom2
    new_numer2 = numer2 * denom1
    result_numer = new_numer1 - new_numer2
    return result_numer, common_denom
