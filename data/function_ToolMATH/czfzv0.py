def sum_of_digits_f(n: int) -> int:
    return sum(int(digit) for digit in str(n))
