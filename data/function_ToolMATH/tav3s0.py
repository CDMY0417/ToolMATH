def calculate_sticks_of_butter_needed(tablespoons_needed: int, tablespoons_per_stick: int) -> int:
    return (tablespoons_needed + tablespoons_per_stick - 1) // tablespoons_per_stick
