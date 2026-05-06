def repeat_decimal(decimal: str, repeat_length: int, extend_to: int) -> str:
    repeat_part = decimal[-repeat_length:]
    full_decimal = decimal + (repeat_part * ((extend_to - len(decimal)) // repeat_length))
    return full_decimal[:extend_to]
