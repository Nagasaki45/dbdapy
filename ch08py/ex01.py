import itertools

import pymc3 as pm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


def acf(trace, lag):
    '''
    Autocorrelation function, based on Pearson correlation
    coefficient.
    '''
    correlation, _ = stats.stats.pearsonr(trace[:-lag], trace[lag:])
    return correlation


def ess(trace):
    '''
    Effective sample size, as defined in Kruschke's "Doing
    Bayesian Data Analysis", 2nd edition, p. 184.
    '''
    significant_autocorrelations = []
    for lag in itertools.count(start=1):
        autocorrelation = acf(trace, lag)
        significant_autocorrelations.append(autocorrelation)
        if autocorrelation < 0.05:
            break
    N = len(trace)
    denominator = 1 + 2 * sum(significant_autocorrelations)
    return N / denominator


data = pd.read_csv('ex01.csv')
subjects = data.subject.unique()

with pm.Model() as model:

    # Model definition
    for subject in subjects:
        subject_prior = pm.Beta('theta_{}'.format(subject), 2, 2)
        subject_data = data[data.subject == subject].y
        pm.Bernoulli('y_{}'.format(subject), subject_prior,
                     observed=subject_data)

    # Inference
    start = pm.find_MAP()
    step = pm.NUTS(scaling=start)  # instantiate sampler
    trace = pm.sample(10000, step, start=start)

pm.traceplot(trace)
pm.stats.summary(trace)

# Per subject effective sample size
for subject in subjects:
    subject_ess = ess(trace.get_values('theta_{}'.format(subject)))
    print('{} ess: {}'.format(subject, subject_ess))

# Subjects bias differences
diffs = {}  # Holds the diff traces
for subj_a, subj_b in itertools.combinations(subjects, 2):
    diff_name = '{} - {}'.format(subj_a, subj_b)
    params = ('theta_{}'.format(subj) for subj in (subj_a, subj_b))
    subj_a_trace, subj_b_trace = (trace.get_values(param) for param in params)
    diffs[diff_name] = subj_a_trace - subj_b_trace

# Plot all the bias differences
plt.figure()
for i, (diff_name, diff_trace) in enumerate(diffs.items(), start=1):
    plt.subplot(len(diffs), 1, i)
    sns.distplot(diff_trace)
    plt.title(diff_name)
    plt.xlim([-1, 1])
plt.tight_layout()

plt.show()
