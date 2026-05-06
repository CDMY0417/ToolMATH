def find_candidate_numbers(k: int, remainder: int, low: int, high: int):
    return [i for i in range(low, high + 1) if i % k == remainder]
