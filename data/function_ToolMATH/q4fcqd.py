def calculate_total_numbers_a(choices_list: list[int]) -> int:
    total_numbers = 1
    for choices in choices_list:
        total_numbers *= choices
    return total_numbers
