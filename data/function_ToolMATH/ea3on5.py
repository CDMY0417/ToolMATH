def is_divisible_by_each_digit(number: int) -> bool:
    digits = [int(d) for d in str(number) if d != '0']
    return all(number % d == 0 for d in digits)
