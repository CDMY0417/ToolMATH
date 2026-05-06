def form_number_from_digits(digits: list[int]) -> int:
    return int(''.join(map(str, digits)))
