def is_divisible_by_3_b(n: int) -> bool:
    digit_sum = sum(int(digit) for digit in str(n))
    return digit_sum % 3 == 0
