def calculate_not_proficient_students(total_students: int, proficient_percentage: float) -> int:
    not_proficient_percentage = 100 - proficient_percentage
    return int(total_students * not_proficient_percentage / 100)
