def compute_inclusion_exclusion_probability(prob_a: float, prob_b: float, prob_a_and_b: float) -> float:
    return prob_a + prob_b - prob_a_and_b
