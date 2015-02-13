p_ill = 0.001
p_healthy = 1 - p_ill
p_positive_given_ill = 0.99
p_negative_given_ill = 1 - p_positive_given_ill
p_positive_given_healthy = 0.05
p_negative_given_healthy = 1 - p_positive_given_healthy

# 1st phase, find p(ill | negative)
# p(ill | negative) = p(negative | ill) * p(ill) / p(negative
p_negative = p_negative_given_ill * p_ill + p_negative_given_healthy * p_healthy
p_ill_given_negative = p_negative_given_ill * p_ill / p_negative
print(paste('1st phase - p(ill | negative): ', p_ill_given_negative))

# Update old values
p_ill = p_ill_given_negative
p_healthy = 1 - p_ill

# 2nd phase, find p(ill | positive)
# p(ill | positive) = p(positive | ill) * p(ill) / p(positive)
p_positive = p_positive_given_ill * p_ill + p_positive_given_healthy * p_healthy
p_ill_given_positive = p_positive_given_ill * p_ill / p_positive
print(paste('2nd phase - p(ill | positive): ', p_ill_given_positive))
# Final result: 0.000208586165048544
