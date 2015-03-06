from scipy.stats import beta
import matplotlib.pyplot as plt

import beta_utils as utils

plt.figure(figsize=(8, 10))

# Question A
plt.subplot(2, 1, 1)
a = b = 50  # Strong prior belief that the coin is fair
prior = beta(a, b)
posterior = beta(*utils.update_beta(a, b, N=10, z=9))
text = '''Update strong prior with\ncontroversial data.
Prior: a = b = {}
N = 10, z = 9
'''.format(a).strip()
utils.prior_posterior_plot(prior, posterior, text)
plt.legend(loc=2)

# Question B
plt.subplot(2, 1, 2)
a = b = .1  # Strong prior belief that the coin is unfair
prior = beta(a, b)
posterior = beta(*utils.update_beta(a, b, N=10, z=9))
text = '''Different prior,\nsame data.
Prior: a = b = {}
N = 10, z = 9
'''.format(a).strip()
utils.prior_posterior_plot(prior, posterior, text)

plt.show()
