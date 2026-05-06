def filter_non_multiples(numbers: list[int], divisor: int) -> list[int]:
    return [n for n in numbers if n % divisor != 0]
