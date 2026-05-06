def fraction_from_repeating_decimal(non_repeating: str, repeating: str):
    n = len(non_repeating)
    k = len(repeating)
    non_rep_part = int(non_repeating) if non_repeating else 0
    rep_part = int(repeating)
    denominator = (10**n) * (10**k - 1)
    numerator = (10**k - 1) * non_rep_part + rep_part
    return (numerator, denominator)
