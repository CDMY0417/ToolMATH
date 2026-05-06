def digit_pair_sums(digits: list[int]) -> list[int]:
    sums = []
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            sums.append(digits[i] + digits[j])
    return sums
