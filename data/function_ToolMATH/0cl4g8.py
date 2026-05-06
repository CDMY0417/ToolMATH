def is_divisible_by_9_c(n: int) -> bool:
    return sum(int(digit) for digit in str(n)) % 9 == 0
