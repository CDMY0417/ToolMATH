def digit_count_in_range(digit: int, start: int, end: int):
    count = 0
    for number in range(start, end + 1):
        count += str(number).count(str(digit))
    return count
