def find_applicable_digits(last_digit: int) -> list:
    return [d for d in range(10) if (d ** 2) % 10 == last_digit]
