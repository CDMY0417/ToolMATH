def is_divisible_n(number: int, divisors: list[int]) -> bool:
    for d in divisors:
        if number % d == 0:
            return True
    return False
