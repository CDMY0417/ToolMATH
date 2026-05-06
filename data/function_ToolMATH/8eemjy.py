def is_abab_form(digits: list[int]) -> bool:
    return len(digits) == 4 and len(set(digits)) == 2 and digits[0] == digits[2] and digits[1] == digits[3]
