def base_2_representation(n: int) -> str:
    if n == 0:
        return '0'
    result = []
    while n > 0:
        remainder = n % 2
        result.append(remainder)
        n //= 2
    return ''.join(map(str, result[::-1]))
