import typing

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import mcmc_utils


def hdi(hdi_tails, *, ax=None):
    '''
    Plot a black line and HDI tails values at the
    bottom of the X axis.
    '''
    if ax is None:
        ax = plt.gca()

    nodge = ax.get_ylim()[1] / 40

    for tail in hdi_tails:
        ax.text(tail, 2 * nodge, f'{tail:.3f}', horizontalalignment='center')

    ax.plot(hdi_tails, [nodge, nodge], color='black', linewidth=2)


def dist(chains, ax=None):
    '''
    Plot distribution analysis of one or more chains
    '''

    if ax is None:
        ax = plt.gca()

    chain = chains.reshape(-1)

    hdi_range = np.mean(np.apply_along_axis(np.percentile, 0, chains, [2.5, 97.5]), axis=1)
    mean = chain.mean()

    sns.distplot(chain, kde=False, ax=ax)
    hdi(hdi_range, ax=ax)
    ax.axvline(mean, color='gray', linestyle='--', linewidth=1)
    ax.text(mean, np.mean(ax.get_ylim()), f'mean = {mean:.2f}', rotation=-90, color='grey')

    ax.set_yticks([])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    return ax


def trace(chains : np.ndarray, axes : typing.List[matplotlib.axes.Axes]=None):
    '''
    Plot trace analysis of one or more chains.
    '''
    if len(chains.shape) == 1:  # One dimension means single chain / trace
        chains = chains[:, np.newaxis]

    ess = np.sum(np.apply_along_axis(mcmc_utils.ess, 0, chains))
    acc_ratio = np.mean(np.apply_along_axis(mcmc_utils.acceptance_ratio, 0, chains))

    if axes is None:
        _, axes = plt.subplots(ncols=2, figsize=(8, 4))
    else:
        assert len(axes) == 2

    dist(chains, ax=axes[0])

    axes[1].plot(chains, linewidth=0.5, alpha=0.5)
    axes[1].annotate(
        f'Eff.Sz = {ess:.1f}\nAcceptance ratio = {acc_ratio:.3f}',
        xy=(0.025, 0.975),
        xycoords='axes fraction',
        verticalalignment='top',
    )

    return axes


def shrinkage(percentage_correct : np.ndarray, estimates : np.ndarray, ax=None):
    '''
    Plot percentage correct and estimate to explore shrinkage.
    '''
    percentage_correct = np.array(percentage_correct)
    estimates = np.array(estimates)

    assert len(percentage_correct) == len(estimates)

    if ax is None:
        ax = plt.gca()

    ax.scatter(
        percentage_correct,
        percentage_correct * 0,
        alpha=0.5,
        label='percentage correct'
    )
    ax.scatter(
        estimates,
        estimates * 0 + 1,
        alpha=0.5,
        label='estimages'
    )
    for origin, target in zip(percentage_correct, estimates):
        ax.arrow(origin, 0.05, target - origin, 0.9, linewidth=0.5, color='grey', alpha=0.5)

    ax.legend()

    ax.set_yticks([])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    return ax
