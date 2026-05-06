def arrange_digits_desc(digits: list[int]) -> int:
    return int(''.join(sorted(map(str, digits), reverse=True)))
