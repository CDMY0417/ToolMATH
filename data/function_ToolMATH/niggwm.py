def filter_multiples(numbers: list[int], divisor: int):
    return [num for num in numbers if num % divisor == 0]
