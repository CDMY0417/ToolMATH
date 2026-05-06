def valid_three_digit_number(number: int) -> bool:
    digits = str(number)
    return len(digits) == 3 and len(set(digits)) == 3
