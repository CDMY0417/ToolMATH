def sum_of_digits_s(n: int) -> int:
    return sum(int(digit) for digit in str(n))
