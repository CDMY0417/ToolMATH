def cubic_root_of_real_number(number: float):
    return number ** (1/3) if number >= 0 else -((-number) ** (1/3))
