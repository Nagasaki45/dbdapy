import time
import warnings
warnings.filterwarnings(action='ignore')

import pymc3 as pm
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import distributions
import seaborn

# Priors constants
theta_prior_a = theta_prior_b = 5

# Generating some synthetic data
theta_true = 0.6
N = 10
z = int(N * theta_true)
data = [1] * z + [0] * (N - z)

# The prior and the likelihood
x = np.linspace(0, 1, 100)
prior = distributions.beta(theta_prior_a, theta_prior_b)

def likelihood(theta, N, z):
    return theta ** z * (1 - theta) ** (N - z)

posterior = distributions.beta(theta_prior_a + z,
                               theta_prior_b + N - z)

# Plotted analytic solution
plt.suptitle('Analytic solution')
plt.subplot(3, 1, 1)
plt.title('Prior')
plt.plot(x, prior.pdf(x))

plt.subplot(3, 1, 2)
plt.title('Likelihood')
plt.plot(x, likelihood(x, N, z))

plt.subplot(3, 1, 3)
plt.title('Posterior')
plt.plot(x, posterior.pdf(x))
plt.tight_layout()

# Do MCMC
with pm.Model():
    # Model design
    theta = pm.Beta('theta', theta_prior_a, theta_prior_b)  # Prior
    y = pm.Bernoulli('y', p=theta, observed=data)  # Likelihood

    # Inference
    start = pm.find_MAP()
    step = pm.NUTS()
    trace = pm.sample(3000, step, start=start, progressbar=False)

pm.traceplot(trace, lines={'theta': theta_true})
pm.stats.summary(trace)

plt.tight_layout()
plt.show()
