def saved_gallons(miles_driven: int, mpg1: int, mpg2: int):
    gallons1 = miles_driven / mpg1
    gallons2 = miles_driven / mpg2
    return gallons1 - gallons2
