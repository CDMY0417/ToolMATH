def exponentiation_result(base: int, number: int) -> int:
    result = 0
    while base ** result < number:
        result += 1
    return result if base ** result == number else -1
