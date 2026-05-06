def count_numbers_with_conditions(max_number: int, units_digit: int, divisor: int) -> int:
    valid_numbers = [i for i in range(10, max_number + 1) if i % 10 == units_digit]
    return len([num for num in valid_numbers if num % divisor == 0])
