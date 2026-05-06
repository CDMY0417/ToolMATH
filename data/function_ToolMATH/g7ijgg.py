def is_divisible_by_9_b(number: int) -> bool:
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum % 9 == 0
