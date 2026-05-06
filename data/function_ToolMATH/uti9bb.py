def max_product_of_two_distinct_numbers(numbers: list[int]) -> int:
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]
