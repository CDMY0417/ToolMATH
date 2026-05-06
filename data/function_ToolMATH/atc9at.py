def modular_product(numbers: list[int], modulus: int) -> int:
    result = 1
    for number in numbers:
        result = (result * number) % modulus
    return result
