def compute_workers_needed(original_workers: int, original_houses: int, original_days: int, target_houses: int, target_days: int) -> int:
    factor_houses = target_houses / original_houses
    factor_time = original_days / target_days
    workers_needed = original_workers * factor_houses * factor_time
    return int(workers_needed)
