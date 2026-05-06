def find_cycle_length(sequence: list[int]) -> int:
    for i in range(1, len(sequence) // 2 + 1):
        if sequence[:i] == sequence[i:2 * i]:
            return i
    return len(sequence)
