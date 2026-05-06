def ending_with_digit(numbers: list[int], digit: int) -> list[int]:
    return [n for n in numbers if n % 10 == digit]
