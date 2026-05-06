def repeating_decimal_length(numerator: int, denominator: int) -> int:
    remainder = numerator % denominator
    remainders = {}
    position = 0
    while remainder != 0: 
        if remainder in remainders:
            return position - remainders[remainder]
        remainders[remainder] = position
        remainder *= 10
        remainder %= denominator
        position += 1
    return 0
