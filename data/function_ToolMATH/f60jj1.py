def probability_of_distinct_suits(total_suits: int, total_cards_per_suit: int) -> float:
    prob_each_suit = total_cards_per_suit / (total_suits * total_cards_per_suit)
    prob_distinct = 1.0
    for i in range(1, total_suits):
        prob_distinct *= (total_suits - i) / total_suits
    return prob_each_suit ** total_suits * prob_distinct
