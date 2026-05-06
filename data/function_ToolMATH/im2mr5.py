def permutations(sequence: list):
    if len(sequence) <= 1:
        return [sequence]
    result = []
    for i, item in enumerate(sequence):
        for perm in permutations(sequence[:i] + sequence[i+1:]):
            result.append([item] + perm)
    return result
