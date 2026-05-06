def is_divisible_by_9_a(number: int) -> bool:
    return sum(int(digit) for digit in str(number)) % 9 == 0
