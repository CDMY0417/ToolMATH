def get_nth_digit_of_consecutive_integers(start: int, end: int, n: int) -> int:
    digits = ''
    for number in range(start, end - 1, -1):
        digits += str(number)
        if len(digits) >= n:
            return int(digits[n - 1])
    return -1
