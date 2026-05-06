def count_digits_of_consecutive_integers(start: int, end: int) -> int:
    digits = 0
    for number in range(start, end - 1, -1):
        digits += len(str(number))
    return digits
