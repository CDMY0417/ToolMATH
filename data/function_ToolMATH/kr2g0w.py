def calculate_total_cost_a(quantities: list[float], prices: list[float]) -> float:
    return sum(q * p for q, p in zip(quantities, prices))
