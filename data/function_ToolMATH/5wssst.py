def count_valid_digits(exclude: int) -> int:
    count = 0
    for digit in range(10):
        if digit != exclude:
            count += 1
    return count
