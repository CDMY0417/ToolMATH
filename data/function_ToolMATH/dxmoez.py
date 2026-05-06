def perform_operations_in_order(numbers: list[float], operators: list[str]) -> float:
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '*':
            result *= numbers[i + 1]
        elif op == '/':
            result /= numbers[i + 1]
        elif op == '+':
            result += numbers[i + 1]
        elif op == '-':
            result -= numbers[i + 1]
    return result
