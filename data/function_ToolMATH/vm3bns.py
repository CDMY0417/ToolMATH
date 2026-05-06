def count_letter_arrangements() -> int:
    vowels = 5  # A, E, I, O, U
    second_letter_choices = 25  # 26 letters - 1 chosen vowel
    third_letter_choices = 24  # 26 letters - 1 chosen vowel - 1 second letter
    return vowels * second_letter_choices * third_letter_choices
