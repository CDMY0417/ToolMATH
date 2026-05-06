def evaluate_absolute_value_equation(a: int, b: int, c: int) -> list[int]:
    abs_value = (c + b) // 2
    return [a + abs_value, a - abs_value]
