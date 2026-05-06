def expected_value_i(prob_event: float, outcome_event: int, prob_other: float, outcome_other: int):
    return prob_event * outcome_event + prob_other * outcome_other
