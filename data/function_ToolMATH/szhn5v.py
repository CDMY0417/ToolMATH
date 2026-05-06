def count_meals_by_entree(entree_price: float, drink_prices: list[float], dessert_prices: list[float], budget: float) -> int:
    count = 0
    for drink_price in drink_prices:
        for dessert_price in dessert_prices:
            if entree_price + drink_price + dessert_price <= budget:
                count += 1
    return count
