def calculate_minimum_workers(task1: int, task2: int, both: int) -> int:
    total_jobs = task1 + task2
    double_counted_jobs = both * 2
    remaining_jobs = total_jobs - double_counted_jobs
    minimum_workers = both + remaining_jobs
    return minimum_workers
