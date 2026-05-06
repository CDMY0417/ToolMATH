def largest_permutation_with_unique_digits(digits: list[int]) -> int:
    return int(''.join(map(str, sorted(digits, reverse=True))))
