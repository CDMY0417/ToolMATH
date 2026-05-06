def two_digit_numbers_with_digit_sum(digit_sum: int):
    result = []
    for tens in range(1, 10):
        for units in range(0, 10):
            if tens + units == digit_sum:
                result.append(tens * 10 + units)
    return result
