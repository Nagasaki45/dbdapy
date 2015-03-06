from scipy.stats import beta
import matplotlib.pyplot as plt

import beta_utils as utils

a = b = 0.1
prior = beta(a, b)
posterior = beta(*utils.update_beta(a, b, N=5, z=4))
text = '''
Prior: a = b = .1
5 flips, 4 heads
'''.strip()
utils.prior_posterior_plot(prior, posterior, text)
plt.legend(loc='best')

plt.show()
