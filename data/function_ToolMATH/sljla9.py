def digit_sum_a(number: int) -> int:
    return sum(int(digit) for digit in str(number))
