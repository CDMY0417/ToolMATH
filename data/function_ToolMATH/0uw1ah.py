def calculate_rides(total_cost: float, entry_fee: float, cost_per_ride: float) -> int:
    return int((total_cost - entry_fee) / cost_per_ride)
