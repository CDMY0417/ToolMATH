def find_first_multiple_in_sequence(sequence: list[int], multiple: int) -> int:
    for x in sequence:
        if x % multiple == 0:
            return x
    return -1
