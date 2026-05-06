def multiples_ending_with_digit(numbers: list[int], digit: int):
    return [num for num in numbers if num % 10 == digit]
