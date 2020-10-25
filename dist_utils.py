import collections


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
