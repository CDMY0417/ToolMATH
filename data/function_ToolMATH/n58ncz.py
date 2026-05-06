def factorial_permutations(choices: list[int]) -> int:
    result = 1
    for choice in choices:
        result *= choice
    return result
