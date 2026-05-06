def sum_of_digits(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))
