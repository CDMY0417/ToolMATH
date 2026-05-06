def repeating_decimal_nth_digit(n: int, cycle_length: int, cycle: str) -> str:
    index = (n - 1) % cycle_length
    return cycle[index]
