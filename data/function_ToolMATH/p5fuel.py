def total_possible_outcomes_a(outcomes_per_event: list[int]) -> int:
    total_outcomes = 1
    for outcomes in outcomes_per_event:
        total_outcomes *= outcomes
    return total_outcomes
