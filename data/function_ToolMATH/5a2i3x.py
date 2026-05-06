def is_divisible_by_any(number: int, divisors: list[int]) -> bool:
    return any(number % d == 0 for d in divisors)
