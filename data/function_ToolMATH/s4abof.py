def apply_coupon(total_cost: float, coupon_value: float, eligibility_threshold: float):
    if total_cost >= eligibility_threshold:
        return total_cost - coupon_value
    return total_cost
