def greatest_positive_two_digit_multiple(num: int) -> int:
    for i in range(99, 9, -1):
        if i % num == 0:
            return i
