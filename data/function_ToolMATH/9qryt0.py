def smallest_digit_not_in_set(digit_set: set[int]) -> int:
    for digit in range(10):
        if digit not in digit_set:
            return digit
