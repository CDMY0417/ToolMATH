def calculate_license_plates(letter_slots: int, digit_slots: int):
    num_letters = 26
    num_digits = 10
    return (num_letters ** letter_slots) * (num_digits ** digit_slots)
