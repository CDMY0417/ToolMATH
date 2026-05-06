def power(base: int, exp: int) -> int:
    result = 1
    for _ in range(exp):
        result *= base
    return result
