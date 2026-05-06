def repeating_decimal_to_fraction_f(non_repeating: int, repeating: int):
    n = len(str(repeating))
    numerator = int(str(non_repeating) + str(repeating)) - non_repeating
    denominator = 10**n - 1
    return numerator, denominator
