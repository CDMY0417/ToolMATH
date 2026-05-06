def repeated_sequence_element(n: int, sequence: list, k: int):
    index = n % k
    return sequence[index - 1] if index != 0 else sequence[-1]
