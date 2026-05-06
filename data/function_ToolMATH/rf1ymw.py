def count_digit_occurrences_a(start: int, end: int, digit: int, position: str):
    count = 0
    for num in range(start, end + 1):
        num_str = str(num).zfill(3)
        if position == 'hundreds' and num_str[0] == str(digit):
            count += 1
        elif position == 'tens' and num_str[1] == str(digit):
            count += 1
        elif position == 'units' and num_str[2] == str(digit):
            count += 1
    return count
