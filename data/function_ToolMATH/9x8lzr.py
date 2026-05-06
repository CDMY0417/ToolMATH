def total_words(alphabet_size: int, max_word_length: int) -> int:
    return sum(alphabet_size ** length for length in range(1, max_word_length + 1))
