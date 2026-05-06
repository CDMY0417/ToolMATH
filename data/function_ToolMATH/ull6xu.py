def multiply_base6(a6: int, b6: int) -> str:
    a10 = int(str(a6), 6)
    b10 = int(str(b6), 6)
    result10 = a10 * b10
    result6 = ''
    while result10:
        result6 = str(result10 % 6) + result6
        result10 //= 6
    return result6 or '0'
