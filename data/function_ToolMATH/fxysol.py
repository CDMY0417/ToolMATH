def digit_in_place(number: float, place: int) -> int:
    decimal_part = str(number).split('.')[1]
    return int(decimal_part[place - 1]) if len(decimal_part) >= place else 0
