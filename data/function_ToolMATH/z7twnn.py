def round_each_to_nearest_ten(numbers: list[int]) -> list[int]:
    return [round(number, -1) for number in numbers]
