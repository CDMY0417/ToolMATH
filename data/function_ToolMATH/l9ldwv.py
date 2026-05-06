def get_digit_at_place(decimal_number: float, place: int):
    str_num = str(decimal_number)
    decimal_part = str_num.split('.')[1]
    return int(decimal_part[place - 1]) if len(decimal_part) >= place else None
