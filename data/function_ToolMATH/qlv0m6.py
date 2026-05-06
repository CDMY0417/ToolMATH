def base10_to_base4(num_base10: int) -> str:
    if num_base10 == 0:
        return '0'
    digits = ''
    while num_base10:
        digits = str(num_base10 % 4) + digits
        num_base10 //= 4
    return digits
