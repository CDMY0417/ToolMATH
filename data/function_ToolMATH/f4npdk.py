def digits_increasing_order(number: int) -> bool:
    digits = [int(digit) for digit in str(number)]
    return all(earlier < later for earlier, later in zip(digits, digits[1:]))
