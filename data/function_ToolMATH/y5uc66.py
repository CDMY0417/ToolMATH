def calculate_yearly_differences(sales: list[float]) -> list[float]:
    return [sales[i + 1] - sales[i] for i in range(len(sales) - 1)]
