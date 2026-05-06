def sum_of_digits_d(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))
