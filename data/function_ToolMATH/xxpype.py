def circle_y_value(x: float, r: float) -> list:
    remainder = r**2 - x**2
    if remainder < 0:
        return []
    elif remainder == 0:
        return [0.0]
    else:
        sqrt_rem = remainder**0.5
        return [sqrt_rem, -sqrt_rem]
