def find_closest_to_target_rounded(numbers: list[float], target: float):
    for number in numbers:
        if round(number, 1) == target:
            return number
    return None
