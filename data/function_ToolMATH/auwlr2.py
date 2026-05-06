def subtract_in_base(num1: int, num2: int, base: int) -> int:
    n1_dec = int(str(num1), base)
    n2_dec = int(str(num2), base)
    result_dec = n1_dec - n2_dec
    result_base = ''
    if result_dec == 0:
        return 0
    while result_dec > 0:
        result_base = str(result_dec % base) + result_base
        result_dec //= base
    return int(result_base)
