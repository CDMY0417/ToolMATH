def remove_multiples(numbers: list[int], factor: int) -> list[int]:
    return [n for n in numbers if n % factor != 0]
