def count_digit_occurrences(max_num: int):
    digit_count = {i: 0 for i in range(10)}
    for num in range(max_num + 1):
        for digit in str(num):
            digit_count[int(digit)] += 1
    return digit_count
