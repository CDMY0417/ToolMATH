def digit_sum_g(number: int) -> int:
    return sum(int(digit) for digit in str(number))
