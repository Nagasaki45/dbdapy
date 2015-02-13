p_ill = 0.001
p_healthy = 1 - p_ill
p_positive_given_ill = 0.99
p_positive_given_healthy = 0.05

# Find p(ill | positive)
# p(ill | positive) = p(positive | ill) * p(ill) / p(positive)
p_positive = p_positive_given_ill * p_ill + p_positive_given_healthy * p_healthy
p_ill_given_positive = p_positive_given_ill * p_ill / p_positive
print(p_ill_given_positive)  # 0.01943463
