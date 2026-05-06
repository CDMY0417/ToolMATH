def letter_cycle_value(position: int) -> int:
    pattern = [1, 2, 1, 0, -1, -2, -1, 0]
    return pattern[(position - 1) % 8]
