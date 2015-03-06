from scipy.optimize import fmin
import numpy as np
import matplotlib.pyplot as plt


def update_beta(a, b, N, z):
    return (z + a, N - z + b)  # See p. 132


def distribution_hdi(distribution, interval_mass=.95):
    # Based on Kruschke R code and http://stackoverflow.com/a/25777507/1224456

    def interval_width(low_tail):
        low_tail_probability = distribution.ppf(low_tail)
        high_tail_probability = distribution.ppf(low_tail + interval_mass)
        return high_tail_probability - low_tail_probability

    # Find low_tail that minimizes interval_width
    best_low_tail = fmin(interval_width, 0, ftol=1e-8, disp=False)[0]
    # Return interval as array([low, high])
    return distribution.ppf([best_low_tail, best_low_tail+ interval_mass])


def prior_posterior_plot(prior, posterior, text, hdi_tails=None):
    x = np.linspace(0, 1, 100)
    plt.text(.05, 2, text)
    plt.plot(x, prior.pdf(x), label='prior')
    plt.plot(x, posterior.pdf(x), label='posterior')

    # Posterior mean annotation
    mean = posterior.mean()
    mean_y = posterior.pdf(mean)
    plt.annotate('mean: {:.2f}'.format(mean), xy=(mean, mean_y),
                 horizontalalignment='center', xytext=(mean, .5 * mean_y),
                 arrowprops=dict(facecolor='black', width=.4, shrink=.05))

    if hdi_tails is not None:
        hdi_plot(posterior, hdi_tails)

    plt.gca().get_yaxis().set_visible(False)  # Disable y ticks


def hdi_plot(distribution, hdi_tails):
    for tail in hdi_tails:
        plt.text(tail, 0, '{:.3f}'.format(tail))
    x = np.linspace(*hdi_tails, num=100)
    plt.fill_between(x, 0, distribution.pdf(x), color='green', alpha=0.3)
