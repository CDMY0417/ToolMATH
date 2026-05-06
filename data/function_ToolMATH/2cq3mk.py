def multiply_modulo(numbers: list[int], mod: int) -> int:
    result = 1
    for number in numbers:
        result = (result * number) % mod
    return result
