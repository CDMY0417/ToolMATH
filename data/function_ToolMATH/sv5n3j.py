def rewrite_subtractions_as_additions(numbers: list[int]) -> list[int]:
    return [n if n >= 0 else -n for n in numbers]
