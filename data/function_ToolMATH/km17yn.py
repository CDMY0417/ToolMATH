def count_divisible_by(numbers: list[int], divisor: int) -> int:
    return sum(1 for number in numbers if number % divisor == 0)
