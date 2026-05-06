def subtract_repeating_decimals(a_non_repeat: float, a_repeat: str, b_non_repeat: float, b_repeat: str) -> float:
    a = float(a_non_repeat) + float('0.' + a_repeat)
    b = float(b_non_repeat) + float('0.' + b_repeat)
    return a - b
