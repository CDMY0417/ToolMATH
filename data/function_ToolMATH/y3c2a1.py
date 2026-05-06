def count_four_digit_integers_without_specific_digits(exclude_digits: list[int]) -> int:
    first_digit_options = [1, 4, 5, 6, 7, 8, 9]
    other_digit_options = [0, 1, 4, 5, 6, 7, 8, 9]
    first_digit_count = len([d for d in first_digit_options if d not in exclude_digits])
    other_digits_count = len([d for d in other_digit_options if d not in exclude_digits])
    return first_digit_count * other_digits_count**3
