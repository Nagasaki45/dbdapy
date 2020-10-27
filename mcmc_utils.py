import itertools

import numpy as np
from scipy import stats


def acf(trace, lag):
    '''
    Autocorrelation function, based on Pearson correlation
    coefficient.
    '''
    if lag <= 0 :
        return 1
    correlation, _ = stats.stats.pearsonr(trace[:-lag], trace[lag:])
    return correlation


def autocorrelations(trace, max_lag):
    '''
    Calculate all autocorrelation values up to `max_lag`. Return an array
    of length `max_lag`.
    '''
    return np.array([acf(trace, lag) for lag in np.arange(max_lag) + 1])


def ess(trace):
    '''
    Effective sample size, as defined in Kruschke's "Doing
    Bayesian Data Analysis", 2nd edition, p. 184.
    '''
    if len(set(trace)) <= 1:
        return float('nan')
    significant_autocorrelations = []
    for lag in itertools.count(start=1):
        autocorrelation = acf(trace, lag)
        significant_autocorrelations.append(autocorrelation)
        if autocorrelation < 0.05:
            break
    N = len(trace)
    denominator = 1 + 2 * sum(significant_autocorrelations)
    return N / denominator


def acceptance_ratio(trace, min_diff=0.0001):
    '''
    The ratio of steps differing by at least `min_diff`.
    '''
    diffs = np.array(trace[1:]) - np.array(trace[:-1])
    abs_diff = np.abs(diffs)
    accepted_steps = abs_diff > min_diff
    return sum(accepted_steps) / len(accepted_steps)


def gelman_rubin(chains):
    '''
    Calculate the Gelman Rubin statistic for the chains.
    '''
    n, m = chains.shape
    chain_means = np.mean(chains, axis=0)
    grand_mean = np.mean(chain_means)
    b = n / (m - 1) * np.sum(np.square(chain_means - grand_mean))
    w = 1 / (m * (n - 1)) * np.sum(np.square(chains - chain_means))
    marginal_posterior_var = (n - 1) / n * w + 1 / n * b
    return np.sqrt(marginal_posterior_var / w)


def running_gelman_rubin_gen(chains):
    '''
    Yield the Gelman Rubin statistic from iteration 2 till last
    iteration.
    '''
    for i in range(2, len(chains)):
        yield gelman_rubin(chains[:i])