def find_repeating_decimal_period(n: int) -> int:
    remainder = 1
    position = 0
    seen_remainders = {}
    while remainder != 0:
        if remainder in seen_remainders:
            return position - seen_remainders[remainder]
        seen_remainders[remainder] = position
        remainder = (remainder * 10) % n
        position += 1
    return 0
