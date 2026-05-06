def probability_of_allergic_reaction(total_breads: int, safe_breads: int, total_meats: int, safe_meats: int, total_sauces: int, safe_sauces: int) -> float:
    non_reaction_probability = (safe_breads / total_breads) * (safe_meats / total_meats) * (safe_sauces / total_sauces)
    reaction_probability = 1 - non_reaction_probability
    return reaction_probability
