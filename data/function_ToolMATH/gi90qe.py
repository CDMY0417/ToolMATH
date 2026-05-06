def opposite_face_sum(numbers: list[int]) -> list[int]:
    return [numbers[i] + numbers[i+1] for i in range(0, len(numbers), 2)]
