def delta_of_sequence(sequence: list[float]) -> list[float]:
    return [sequence[i+1] - sequence[i] for i in range(len(sequence) - 1)]
