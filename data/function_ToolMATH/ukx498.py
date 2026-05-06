def generate_two_digit_numbers(digits: set[int]) -> set[int]:
    return {int(str(a) + str(b)) for a in digits for b in digits}
