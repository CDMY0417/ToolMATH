def students_taking_neither(total_students: int, only_first: int, only_second: int, both: int) -> int:
    return total_students - only_first - only_second - both
