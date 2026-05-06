def count_answer_combinations(choices_per_question: list[int]) -> int:
    total_combinations = 1
    for choices in choices_per_question:
        total_combinations *= choices
    return total_combinations
