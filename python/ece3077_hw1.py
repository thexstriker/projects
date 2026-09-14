import numpy as np

rng = np.random.default_rng(3077)
n_trials = 10000
die4 = rng.integers(1, 5, size=n_trials)
die5 = rng.integers(1, 6, size=n_trials)
product_is_even = (die4 * die5) % 2 == 0
sum_condition = (
((die4 + die5) <= 3)
| ((die4 + die5) > 7)
)
event = product_is_even & sum_condition
estimated_probability = np.mean(event)

print(
f"Estimated probability: "
f"{estimated_probability:.4f}"
)
