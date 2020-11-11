import collections

import scipy.optimize as soptimize
import scipy.stats as sstats


def hdi(dist, interval_mass=.95):
    '''
    Calculate the HDI of a given distribution. Based on Kruschke's R code
    and http://stackoverflow.com/a/25777507/1224456.

    dist : most have ppf method to convert a probability to a parameter.
    '''

    def interval_width(low_tail_prob):
        low_tail = dist.ppf(low_tail_prob)
        high_tail = dist.ppf(low_tail_prob + interval_mass)
        return high_tail - low_tail

    # Find low_tail_probability that minimizes interval_width
    low_tail_prob = 1 - interval_mass  # Initial value
    res = soptimize.fmin(interval_width, low_tail_prob, disp=False)
    low_tail_prob = res[0]
    # Return interval as array([low, high])
    return dist.ppf([low_tail_prob, low_tail_prob + interval_mass])

  
GammaParams = collections.namedtuple('GammaParams', ['shape', 'scale'])


def gamma_params_from_mean_and_sd(mean : float, sd: float) -> GammaParams:
    """
    Convert mean and sd into `GammaParams` (shape and scale).
    """
    # Calculations are based on info from wikipedia
    # http://en.wikipedia.org/wiki/Gamma_distribution
    return GammaParams((mean / sd) ** 2, sd ** 2 / mean)


def gamma_params_from_mode_and_sd(mode : float, sd: float) -> GammaParams:
    """
    Convert mode and sd into `GammaParams` (shape and scale).
    """
    # Calculations are based on info from wikipedia
    # http://en.wikipedia.org/wiki/Gamma_distribution
    scale = ((mode ** 2 + 4 * sd ** 2) ** 0.5 - mode) / 2
    shape = (sd / scale) ** 2
    return GammaParams(shape, scale)


BetaParams = collections.namedtuple('BetaParams', ['a', 'b'])


def beta_params_from_w_and_k(w: float, k: float) -> BetaParams:
    """
    Convert mode and concentration into `BetaParams` (a and b).
    """
    # Calculations are based on info from wikipedia
    # https://en.wikipedia.org/wiki/Beta_distribution#Mode_and_concentration
    return BetaParams(w * (k - 2) + 1, (1 - w) * (k - 2) + 1)


def update_beta(prior : sstats.beta, N : int, z : int):
    '''
    Update beta distribution prior with `z` positives in `N`
    attempts.
    '''
    a, b = prior.args
    return sstats.beta(a + z, b + N - z)  # See p. 132