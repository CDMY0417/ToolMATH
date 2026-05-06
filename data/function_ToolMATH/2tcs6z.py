def words_without_specific_letter(alphabet_size: int, excluded_letter_count: int, word_length: int) -> int:
    return (alphabet_size - excluded_letter_count) ** word_length
