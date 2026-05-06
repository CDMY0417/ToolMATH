def count_students_in_at_least_one_course(history_count: int, math_count: int, overlap_count: int) -> int:
    return history_count + math_count - overlap_count
