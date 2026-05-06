def decompose_decimal_to_powers_of_ten(decimal_number: float):
    components = str(decimal_number).split('.')
    integer_part = int(components[0]) if components[0] else 0
    fractional_part = components[1] if len(components) > 1 else '0'
    terms = []
    power_of_ten = len(str(integer_part)) - 1
    for digit in str(integer_part):
        if digit != '0':
            terms.append(int(digit) * (10 ** power_of_ten))
        power_of_ten -= 1
    for i, digit in enumerate(fractional_part):
        if digit != '0':
            terms.append(int(digit) * (10 ** -(i + 1)))
    return terms
