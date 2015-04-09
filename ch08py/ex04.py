import seaborn as sns
import matplotlib.pyplot as plt
import pymc3 as pm
import pandas as pd

with pm.Model() as model:
    # Model definition
    theta_a = pm.Beta('theta_a', .5, .5)
    theta_b = pm.Beta('theta_b', .5, .5)

    # Sampling the prior
    step = pm.NUTS()
    trace = pm.sample(5000, step)

data = pd.DataFrame({t: trace.get_values(t) for t in ('theta_a', 'theta_b')})

# Plot
sns.jointplot('theta_a', 'theta_b', data, kind="hex", stat_func=None)

plt.figure()
sns.distplot(data['theta_a'] - data['theta_b'])
plt.suptitle('theta_a - theta_b')
plt.show()
