def count_multiples_of_three_in_list(numbers: list[int]) -> int:
    return sum(1 for number in numbers if number % 3 == 0)
