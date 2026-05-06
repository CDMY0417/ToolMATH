def compound_interest(principal: float, rate: float, years: int, compounds_per_year: int) -> float:
    return principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
