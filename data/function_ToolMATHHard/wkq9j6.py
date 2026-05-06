def tan_difference(tan_alpha: float, tan_beta: float):
    'Compute tan(alpha-beta) given tan alpha and tan beta.'
    return (tan_alpha - tan_beta) / (1 + tan_alpha * tan_beta)
