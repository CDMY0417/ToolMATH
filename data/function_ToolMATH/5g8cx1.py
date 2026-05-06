def add_base_12(num1: list[int], num2: list[int]) -> list[int]:
    # Reverse the lists to make addition easier
    num1 = num1[::-1]
    num2 = num2[::-1]
    max_len = max(len(num1), len(num2))
    carry = 0
    result = []

    for i in range(max_len):
        digit1 = num1[i] if i < len(num1) else 0
        digit2 = num2[i] if i < len(num2) else 0
        # Base 12 addition
        total = digit1 + digit2 + carry
        carry = total // 12
        result.append(total % 12)

    if carry > 0:
        result.append(carry)

    # Reverse result to get the correct order
    return result[::-1]
