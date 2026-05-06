def units_digit_of_power_c(base: int, exponent: int):
    ones_digit_patterns = {1: [1], 2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 4: [4, 6], 5: [5], 6: [6], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1], 0: [0]}
    last_digit = base % 10
    pattern = ones_digit_patterns[last_digit]
    pattern_length = len(pattern)
    index = (exponent % pattern_length) - 1
    return pattern[index]
