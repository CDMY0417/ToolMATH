def first_occurrence_of_difference(differences: list[int], threshold: int) -> int:
    for i, diff in enumerate(differences):
        if diff >= threshold:
            return i
    return -1
