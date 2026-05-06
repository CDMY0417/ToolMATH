def evaluate_multiplication_expression(numbers: list[int]) -> int:
    result = 1
    for number in numbers:
        result *= number
    return result
