def compute_pages_for_budget(budget_cents: float, cost_per_page_cents: float) -> int:
    return int(budget_cents // cost_per_page_cents)
