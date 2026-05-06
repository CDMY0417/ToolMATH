def find_integer_square_coefficient(number: int):
    possible_root = int(number**0.5)
    if possible_root**2 == number:
        return possible_root
    return None
