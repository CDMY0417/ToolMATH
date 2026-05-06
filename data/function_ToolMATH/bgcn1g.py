def digit_sum_mod_9(number: int) -> int:
    return sum(int(digit) for digit in str(number)) % 9
