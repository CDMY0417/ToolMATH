def get_repeating_sequence(numerator: int, denominator: int) -> str:
    from decimal import Decimal, getcontext
    getcontext().prec = 102  # Set precision high enough to capture the repeating sequence
    decimal_rep = str(Decimal(numerator) / Decimal(denominator)).split('.')[1]
    # Assume repeating sequence starts immediately after the decimal.
    for i in range(1, len(decimal_rep)):
        seq = decimal_rep[:i]
        repeated = seq * (len(decimal_rep) // len(seq))
        if decimal_rep.startswith(repeated):
            return seq
    return decimal_rep
