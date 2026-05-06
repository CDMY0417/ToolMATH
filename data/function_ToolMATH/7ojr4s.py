def divide_base6(number_base6: int) -> str:
    a10 = int(str(number_base6), 6)
    result10 = a10 // 2
    result6 = ''
    while result10:
        result6 = str(result10 % 6) + result6
        result10 //= 6
    return result6 or '0'
