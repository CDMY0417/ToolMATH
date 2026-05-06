def sum_of_digits_ae(number: int) -> int:
    return sum(int(digit) for digit in str(number))
