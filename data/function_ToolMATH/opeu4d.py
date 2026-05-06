def heron_area(a: int, b: int, c: int) -> float:
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
