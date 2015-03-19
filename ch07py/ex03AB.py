import numpy as np
import matplotlib.pyplot as plt
import seaborn


def prior(theta):
    return (np.cos(4 * np.pi * theta) + 1) ** 2 / 1.5

x = np.linspace(0, 1, 100)
plt.plot(x, prior(x))
plt.title('Alternative prior')
plt.xlabel('$\Theta$')
plt.show()
