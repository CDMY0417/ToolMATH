def calculate_cycle_length(numerator: int, denominator: int) -> int:
    remainders = {}
    remainder = numerator % denominator
    position = 0
    while remainder not in remainders:
        remainders[remainder] = position
        remainder = (remainder * 10) % denominator
        position += 1
        if remainder == 0:
            return 0  # Terminates, no repeating cycle
    return position - remainders[remainder]
