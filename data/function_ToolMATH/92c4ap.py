def convert_furlongs_fortnight_to_miles_day(furlongs_per_fortnight: float) -> float:
    miles_per_furlong = 1 / 8
    fortnights_per_day = 1 / 14
    return furlongs_per_fortnight * miles_per_furlong * fortnights_per_day
