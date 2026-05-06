def multiply_choices(choices: list[int]) -> int:
    total = 1
    for choice in choices:
        total *= choice
    return total
