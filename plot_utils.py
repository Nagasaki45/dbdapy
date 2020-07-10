import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import mcmc_utils


def hdi(hdi_tails, *, ax=None, text_height=0.1):
    '''
    Plot a black line and HDI tails values at the
    bottom of the X axis.
    '''
    if ax is None:
        ax = plt.gca()

    for tail in hdi_tails:
        ax.text(tail, text_height, f'{tail:.3f}', horizontalalignment='center')

    ax.plot(hdi_tails, [0, 0], color='black', linewidth=2)


def trace(chains : np.ndarray):
    '''
    Plot trace analysis of one or more chains.
    '''
    if len(chains.shape) == 1:  # One dimension means single chain / trace
        chains = chains[:, np.newaxis]

    ess = np.sum(np.apply_along_axis(mcmc_utils.ess, 0, chains))
    acc_ratio = np.mean(np.apply_along_axis(mcmc_utils.acceptance_ratio, 0, chains))
    hdi_range = np.mean(np.apply_along_axis(np.percentile, 0, chains, [2.5, 97.5]), axis=1)

    fig, axes = plt.subplots(nrows=3, figsize=(4, 6), sharex=True)

    for chain in chains.T:
        sns.distplot(chain, ax=axes[0], hist=False)
    axes[1].plot(chains[-100:], np.arange(-100, 0) + len(chains), linewidth=0.5)
    axes[2].plot(chains[:100], range(100), linewidth=0.5)

    hdi(hdi_range, ax=axes[0])
    axes[0].annotate(
        f'Eff.Sz = {ess:.1f}',
        xy=(0.025, 0.95),
        xycoords='axes fraction',
        verticalalignment='top',
    )
    axes[0].set_yticks([])

    axes[1].set_title('End of chain')
    axes[1].annotate(
        f'Acceptance ratio = {acc_ratio:.3f}',
        xy=(0.025, 0.05),
        xycoords='axes fraction',
    )

    axes[2].set_title('Beginning of chain')

    fig.tight_layout()

    return fig, axes
