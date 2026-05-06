def calculate_problems_to_solve(required_points: float, points_per_correct: int) -> int:
    return int(required_points // points_per_correct) + 1
