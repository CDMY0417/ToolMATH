def minimum_workers_for_profit(fixed_costs: float, hourly_cost_per_worker: float, revenue_per_worker_per_hour: float, work_hours: int):
    return int((fixed_costs / ((revenue_per_worker_per_hour - hourly_cost_per_worker) * work_hours))) + 1
