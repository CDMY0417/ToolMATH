def digit_position_in_repetend(position: int, repetend_length: int) -> int:
    return (position - 1) % repetend_length + 1
