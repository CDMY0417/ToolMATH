def num_base_palindromes_of_length(length: int, base: int) -> int:
    if length == 1:
        return base - 1  # excluding '0'
    half_length = length // 2
    return base ** half_length
