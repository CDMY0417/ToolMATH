def is_divisible_by_3_h(number: int) -> bool:
    return sum(int(digit) for digit in str(number)) % 3 == 0
