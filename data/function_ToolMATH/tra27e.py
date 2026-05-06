def years_to_recuperate_costs(installation_cost: int, annual_maintenance: int, annual_savings: int) -> int:
    effective_savings_per_year = annual_savings - annual_maintenance
    years = installation_cost / effective_savings_per_year
    return int(years) + 1 if years > int(years) else int(years)
