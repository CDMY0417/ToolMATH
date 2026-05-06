def calculate_students_taking_neither(total_students: int, taking_1: int, taking_2: int, taking_both: int) -> int:
    taking_either = taking_1 + taking_2 - taking_both
    taking_neither = total_students - taking_either
    return taking_neither
