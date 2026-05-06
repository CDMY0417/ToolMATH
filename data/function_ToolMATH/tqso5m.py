def pairwise_differences_a(numbers: list[int]) -> list[int]:
    differences = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            differences.append(numbers[j] - numbers[i])
    return differences
