def count_digit_occurrences_in_range(start: int, end: int, digit: str) -> int:
    count = 0
    for number in range(start, end + 1):
        count += str(number).count(digit)
    return count
