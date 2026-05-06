def octal_addition(num1: str, num2: str) -> str:
    len1, len2 = len(num1), len(num2)
    max_len = max(len1, len2)
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    carry = 0
    result = ''
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        result = str(digit_sum % 8) + result
        carry = digit_sum // 8
    if carry:
        result = '1' + result
    return result
