def largest_number_with_digits(digits: list[int]) -> int:
    return int(''.join(map(str, sorted(digits, reverse=True))))
