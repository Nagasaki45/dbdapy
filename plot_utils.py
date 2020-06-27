import matplotlib.pyplot as plt


def hdi(hdi_tails, *, ax=None):
    '''
    Plot a black line and HDI tails values at the
    bottom of the X axis.
    '''
    if ax is None:
        ax = plt.gca()

    for tail in hdi_tails:
        ax.text(tail, 0, f'{tail:.3f}', horizontalalignment='center')

    ax.plot(hdi_tails, [0, 0], color='black', linewidth=2)
