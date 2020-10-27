import functools
import typing

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import mcmc_utils


def ax_plotter(f):
    '''
    A wrapper for functions that accept an ax and return an ax.
    '''
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs.get('ax') is None:
            kwargs['ax'] = plt.gca()
        f(*args, **kwargs)
        return kwargs['ax']
    return wrapper


@ax_plotter
def hdi(hdi_tails, ax):
    '''
    Plot a black line and HDI tails values at the
    bottom of the X axis.
    '''
    nodge = ax.get_ylim()[1] / 40

    for tail in hdi_tails:
        ax.text(tail, 2 * nodge, f'{tail:.3f}', horizontalalignment='center')

    ax.plot(hdi_tails, [nodge, nodge], color='black', linewidth=2)


def _dist(chain, density, ax, **kwargs):
    sns.distplot(chain, kde=density, hist=not density, ax=ax, **kwargs)
    ax.set(xlabel='param value', yticks=[])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)


def _dist_single_chain(chain, ax):

    hdi_range = np.percentile(chain, [2.5, 97.5])
    mean = chain.mean()

    _dist(chain, density=False, ax=ax)
    hdi(hdi_range, ax=ax)
    ax.axvline(mean, color='gray', linestyle='--', linewidth=1)
    ax.text(mean, np.mean(ax.get_ylim()), f'mean = {mean:.2f}', rotation=-90, color='grey')


@ax_plotter
def dist(chains, ax, compare_chains=False):
    '''
    Plot distribution analysis of one or more chains
    '''
    if compare_chains:
        for chain in chains.T:
            _dist(chain, density=True, kde_kws={'linewidth': 1, 'alpha': 0.5}, ax=ax)
    else:
        _dist_single_chain(chains.reshape(-1), ax=ax)


def _annotate(text, ax):
    ax.annotate(
        text,
        xy=(0.975, 0.975),
        xycoords='axes fraction',
        verticalalignment='top',
        horizontalalignment='right',
    )


@ax_plotter
def trace(chains : np.ndarray, ax):
    '''
    Trace plot.
    '''
    ess = np.sum(np.apply_along_axis(mcmc_utils.ess, 0, chains))
    acc_ratio = np.mean(np.apply_along_axis(mcmc_utils.acceptance_ratio, 0, chains))

    ax.plot(chains, linewidth=0.5, alpha=0.5)
    ax.set(xlabel='iterations', ylabel='param value')
    _annotate(f'Eff.Sz = {ess:.1f}\nAcceptance ratio = {acc_ratio:.3f}', ax)


@ax_plotter
def autocorrelation(chains: np.ndarray, ax, max_lag=30):
    '''
    Autocorrelation plot
    '''
    acs = np.apply_along_axis(
        lambda x: mcmc_utils.autocorrelations(x, max_lag),
        0,
        chains,
    )

    ax.plot(np.arange(max_lag) + 1, acs)


def dist_and_trace(chains, axes=None):
    '''
    Helper to plot dist and trace side by side.
    '''
    if axes is None:
        _, axes = plt.subplots(ncols=2, figsize=(8, 3))
    dist(chains, ax=axes[0])
    trace(chains, ax=axes[1])
    return axes


def trace_analysis(chains : np.ndarray, max_lag : int=30, axes : np.array=None):
    '''
    Plot trace analysis of one or more chains.
    '''
    if len(chains.shape) == 1:  # One dimension means single chain / trace
        chains = chains[:, np.newaxis]

    ess = np.sum(np.apply_along_axis(mcmc_utils.ess, 0, chains))
    mcse = np.std(chains) / np.sqrt(ess)

    if axes is None:
        _, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 5))
    assert axes.shape == (2, 2)

    # Top left: trace plot
    trace(chains, ax=axes[0, 0])

    # Top right: lag analysis
    autocorrelation(chains, ax=axes[0, 1])
    axes[0, 1].set(xlabel='lag', ylabel='autocorrelation')

    # Bottom left: shrink factor
    running_gelman_rubin = list(mcmc_utils.running_gelman_rubin_gen(chains))
    axes[1, 0].plot(np.arange(2, len(chains)), running_gelman_rubin)
    axes[1, 0].set(xlabel='last iteration', ylabel='gelman-rubin')

    # Bottom right: density
    dist(chains, compare_chains=True, ax=axes[1, 1])
    _annotate(f'MCSE = {mcse:.5f}', axes[1, 1])

    plt.tight_layout()
    return axes


@ax_plotter
def shrinkage(percentage_correct : np.ndarray, estimates : np.ndarray, ax):
    '''
    Plot percentage correct and estimate to explore shrinkage.
    '''
    percentage_correct = np.array(percentage_correct)
    estimates = np.array(estimates)

    assert len(percentage_correct) == len(estimates)

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


def param_comparison(trace, param, comparison, scatter_sample=30, axes=None):

    if axes is None:
        n = len(comparison)
        _, axes = plt.subplots(nrows=n, ncols=n, figsize=(8, 8))

    x = trace[param]

    sample = np.random.randint(len(x[-1]), size=scatter_sample)

    for i, first in enumerate(comparison):
        dist(x[first], ax=axes[i, i])
        axes[i, i].set(title=f'{param}[{first}]')
        for j, second in enumerate(comparison[i + 1:], start=i + 1):
            dist(x[first] - x[second], ax=axes[i, j])
            axes[i, j].set(title=f'{param}[{first}] - {param}[{second}]')
            axes[j, i].scatter(x[first][sample], x[second][sample])
            axes[j, i].set(xlabel=f'{param}[{first}]', ylabel=f'{param}[{second}]')

    plt.gcf().tight_layout()

    return axes
