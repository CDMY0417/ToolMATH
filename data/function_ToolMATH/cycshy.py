def calculate_time_with_different_workers(total_work: float, num_workers: int, single_worker_rate: float):
    return total_work / (num_workers * single_worker_rate)
