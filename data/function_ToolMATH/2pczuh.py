def sum_of_digits_y(number: int) -> int:
    return sum(int(digit) for digit in str(number))
