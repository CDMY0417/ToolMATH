def sum_of_digits_b(num: int) -> int:
    return sum(int(digit) for digit in str(num))
