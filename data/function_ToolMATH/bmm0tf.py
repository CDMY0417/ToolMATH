def repeating_digit(digits: str, k: int) -> str:
    index = (k - 1) % len(digits)
    return digits[index]
