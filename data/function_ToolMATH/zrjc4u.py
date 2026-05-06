def ounces_to_pounds(ounces: int):
    pounds = ounces // 16
    remainder = ounces % 16
    return pounds, remainder
