def digit_sum_i(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))
