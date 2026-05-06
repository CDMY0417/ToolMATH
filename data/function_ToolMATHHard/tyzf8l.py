def sum_integers_digit_length_constraints():
    # Numbers with 2 digits in base2 and 1 digit in base3: 2
    # 4 digits base2 and 2 digits base3: 9,10,11
    # 6 digits base2 and 3 digits base3: 33..63
    # Sum all: 2 + (9+10+11) + sum(33..63)
    return 2 + (9+10+11) + (33+63)*31/2
