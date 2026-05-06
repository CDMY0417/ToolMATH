def number_of_choices(exponents: list[int]) -> int:
    total_choices = 1
    for exp in exponents:
        total_choices *= (exp + 1)
    return total_choices
