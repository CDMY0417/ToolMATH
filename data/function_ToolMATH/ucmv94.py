def interval_contains_divisible_number(start: int, end: int, divisor: int) -> bool:
    for number in range(start, end + 1):
        if number % divisor == 0:
            return True
    return False
