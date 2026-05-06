def count_digit_as_units(digit: int, start: int, end: int) -> int:
    count = 0
    for num in range(start, end + 1):
        if num % 10 == digit:
            count += 1
    return count
