def is_divisible_by_3(number: int) -> bool:
    return sum(int(digit) for digit in str(number)) % 3 == 0
