def count_neither_subject(total_students: int, only_subject_a: int, only_subject_b: int, both_subjects: int) -> int:
    return total_students - only_subject_a - only_subject_b - both_subjects
