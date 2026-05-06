def subtract_fractions_d(numer1: int, denom1: int, numer2: int, denom2: int):
    numer = numer1 * denom2 - numer2 * denom1
    denom = denom1 * denom2
    return numer, denom
