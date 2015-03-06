from scipy.stats import beta
import matplotlib.pyplot as plt

import beta_utils as utils

plt.figure(figsize=(8, 10))

# Question A
plt.subplot(2, 1, 1)
a, b = 1, 1
prior = beta(a, b)
a, b = utils.update_beta(a, b, N=100, z=58)
posterior = beta(a, b)
text = 'From uniform to 100 flips,\n58 heads'
hdi_tails = utils.distribution_hdi(posterior)
utils.prior_posterior_plot(prior, posterior, text, hdi_tails=hdi_tails)
plt.legend(loc=2)

# Question B
plt.subplot(2, 1, 2)
prior = posterior
a, b = utils.update_beta(a, b, N=100, z=57)
posterior = beta(a, b)
text = 'Additional 100 flips,\n57 heads'
hdi_tails = utils.distribution_hdi(posterior)
utils.prior_posterior_plot(prior, posterior, text, hdi_tails=hdi_tails)

plt.show()
