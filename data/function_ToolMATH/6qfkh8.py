def filter_divisible_numbers(numbers: list[int], divisor: int):
    return [number for number in numbers if number % divisor == 0]
