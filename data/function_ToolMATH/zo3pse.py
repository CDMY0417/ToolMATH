import math

def simplified_radical(number: float):
    square_factor = int(math.sqrt(number))
    while square_factor > 1:
        if number % (square_factor * square_factor) == 0:
            simple_form = number // (square_factor * square_factor)
            return square_factor, simple_form
        square_factor -= 1
    return 1, number
