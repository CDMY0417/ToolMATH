def calculate_neither_students(total_students: int, only_math_students: int, only_physics_students: int, both_math_physics: int) -> int:
    return total_students - only_math_students - only_physics_students - both_math_physics
