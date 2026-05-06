def angle_between_clock_numbers(number1: int, number2: int) -> float:
    degrees_per_hour = 360 / 12
    return abs(number1 - number2) * degrees_per_hour
