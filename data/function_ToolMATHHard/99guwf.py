from fractions import Fraction

def sum_first_digits_of_fraction_sum(fractions, digits: int):
    # Sum first digits after decimal of sum of fractions
    s = Fraction(0,1)
    for num,den in fractions:
        s += Fraction(num,den)
    rem = s.numerator % s.denominator
    total = 0
    for _ in range(digits):
        rem *= 10
        digit = rem // s.denominator
        rem = rem % s.denominator
        total += digit
    return total
