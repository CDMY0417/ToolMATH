def repeating_decimal_length_a(a: int, b: int) -> int:
    from math import gcd
    b_no_2_5 = b // gcd(b, 10)
    length = 1
    remainder = 10 % b_no_2_5
    remainders = {remainder}
    while remainder:
        remainder = (remainder * 10) % b_no_2_5
        if remainder in remainders:
            break
        remainders.add(remainder)
        length += 1
    return length
