def is_alphabetical(sequence: list[str]) -> bool:
    return all(sequence[i] <= sequence[i+1] for i in range(len(sequence) - 1))
