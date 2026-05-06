def convert_horsepower_to_kilowatts(horsepower: float, conversion_factor: float):
    kilowatts = horsepower / conversion_factor
    return round(kilowatts)
