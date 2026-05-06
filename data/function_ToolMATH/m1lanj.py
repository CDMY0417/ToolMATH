def find_least_clock_equivalent(start_hour: int, modulus: int) -> int:
    hour = start_hour + 1
    while True:
        if (hour**2 - hour) % modulus == 0:
            return hour
        hour += 1
