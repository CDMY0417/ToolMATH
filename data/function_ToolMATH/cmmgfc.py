def generate_offsets(numbers: list[int]) -> list[int]:
    offsets = []
    for number in numbers:
        offsets.append(number + 1)
        offsets.append(number + 2)
    return offsets
