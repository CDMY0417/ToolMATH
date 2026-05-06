def sum_of_digits_ac(number: float):
    digits = str(number).replace('.', '')
    return sum(int(digit) for digit in digits)
