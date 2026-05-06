def add_in_base(num1: str, num2: str, base: int) -> str:
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    carry = 0
    result = []
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(num1[i], base) + int(num2[i], base) + carry
        carry = digit_sum // base
        result.append(digit_sum % base)
    if carry:
        result.append(carry)
    return ''.join(map(str, result[::-1]))
