def valid_single_digit_replacements(current_sum: int):
    return [n for n in range(10) if (current_sum + n) % 3 == 0]
