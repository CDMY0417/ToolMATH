def base_conversion_digits(base16_number: str) -> int:
    base10_number = int(base16_number, 16)
    binary_digits = base10_number.bit_length()
    return binary_digits
