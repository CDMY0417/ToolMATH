def yards_to_miles_and_remaining_yards(yards: int):
    miles = yards // 1760
    remaining_yards = yards % 1760
    return miles, remaining_yards
