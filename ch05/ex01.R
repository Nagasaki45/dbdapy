p_ill = 0.001
p_healthy = 1 - p_ill
p_positive_g_ill = 0.99
p_positive_g_healthy = 0.05

# Find p(ill | positive)
# p(ill | positive) = p(positive | ill) * p(ill) / p(positive)
p_positive = p_positive_g_ill * p_ill + p_positive_g_healthy * p_healthy
p_ill_g_positive = p_positive_g_ill * p_ill / p_positive
print(p_ill_g_positive)  # 0.01943463

p_ill = p_ill_g_positive  # Updating the prior

p_healthy = 1 - p_ill
p_negative_g_ill = 1 - p_positive_g_ill

# Find p(ill | negative)
# p(ill | negative) = p(negative | ill) * p(ill) / p(negative)
p_positive = p_positive_g_ill * p_ill + p_positive_g_healthy * p_healthy
p_negative = 1 - p_positive
p_ill_g_negative = p_negative_g_ill * p_ill / p_negative
print(p_ill_g_negative)  # 0.0002085862
