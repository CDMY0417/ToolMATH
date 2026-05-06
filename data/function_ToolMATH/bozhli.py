def count_valid_codes_no_repeats(total_digits: int, code_length: int) -> int:
    from math import prod
    choices = [total_digits - i for i in range(code_length)]
    return prod(choices)
