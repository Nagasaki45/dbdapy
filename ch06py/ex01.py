from scipy.stats import beta
import matplotlib.pyplot as plt

import beta_utils as utils

plt.figure(figsize=(10, 10))

# Question A
plt.subplot(4, 1, 1)
a, b = 4, 4
prior = beta(a, b)
plt.text(0.05, 2, 'First flip, head')
a, b = utils.update_beta(a, b, N=1, z=1)
posterior = beta(a, b)
utils.prior_posterior_plot(prior, posterior, 'First flip, head')

# Question B
plt.subplot(4, 1, 2)
prior = posterior
a, b = utils.update_beta(a, b, N=1, z=1)
posterior = beta(a, b)
utils.prior_posterior_plot(prior, posterior, 'Second flip, head again')

# Question C
plt.subplot(4, 1, 3)
prior = posterior
a, b = utils.update_beta(a, b, N=1, z=0)
posterior = beta(a, b)
utils.prior_posterior_plot(prior, posterior, '3rd flip, tail')

# Question D
plt.subplot(4, 1, 4)
a, b = 4, 4
prior = beta(a, b)
a, b = utils.update_beta(a, b, N=3, z=2)
posterior = beta(a, b)
utils.prior_posterior_plot(prior, posterior, 'All together: 3 flips, THH')

plt.legend(loc=3)
plt.show()
