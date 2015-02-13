p_ill = 0.01943463  # Prior updated by ex01 posterior
p_healthy = 1 - p_ill
p_positive_given_ill = 0.99
p_positive_given_healthy = 0.05
p_negative_given_ill = 1 - p_positive_given_ill

# Find p(ill | negative)
# p(ill | negative) = p(negative | ill) * p(ill) / p(negative)
p_positive = p_positive_given_ill * p_ill + p_positive_given_healthy * p_healthy
p_negative = 1 - p_positive
p_ill_given_negative = p_negative_given_ill * p_ill / p_negative
print(p_ill_given_negative)  # 0.0002085862
