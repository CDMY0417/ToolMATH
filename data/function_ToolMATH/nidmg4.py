def count_palindrome_combinations(digits: list[int], size: int) -> int:
    return len(digits) ** (size // 2 + size % 2)
