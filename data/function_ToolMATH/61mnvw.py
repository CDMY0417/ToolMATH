def filter_two_digit_numbers(numbers: list[int]) -> list[int]:
    return [num for num in numbers if 10 <= num < 100]
