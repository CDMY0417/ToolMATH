def binary_to_octal(binary_str: str) -> str:
    length = len(binary_str)
    if length % 3 != 0:
        binary_str = '0' * (3 - length % 3) + binary_str
    octal_str = ''
    for i in range(0, len(binary_str), 3):
        octal_digit = int(binary_str[i:i+3], 2)
        octal_str += str(octal_digit)
    return octal_str
