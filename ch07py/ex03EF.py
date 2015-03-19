'''
E)
This case fail to represent the posterior because the trace never
leaves the area around 0.
The reason is the small proposal SD and the fact that there is
a boundary between the modes of the prior distribution.

F)
Same issue. Change starting point of the Metropolis algorithm
to 0.99 to see the same behavior from the other side of the
multi-modal prior distribution.
'''
import itertools

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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


def acceptance_ratio(trace, min_diff=0.0001):
    diffs = np.array(trace[1:]) - np.array(trace[:-1])
    abs_diff = np.abs(diffs)
    not_accepted_steps = abs_diff < min_diff
    return 1 - sum(not_accepted_steps) / (len(trace) - 1)


# Specify the data, to be used in the likelihood function
data = [0, 1, 1]

def likelihood(theta, data):
    '''Bernoulli likelihood function'''
    if theta > 1 or theta < 0:
        return 0
    z = sum(data)
    N = len(data)
    return theta ** z * (1 - theta) ** (N - z)

# Define the prior density function
def prior(theta):
    return (np.cos(4 * np.pi * theta) + 1) ** 2 / 1.5

# Define the relative probability of the target distribution,
# as a function of vector theta. For our application, this
# target distribution is the unnormalized posterior distribution.
def target_relative_probability(theta, data):
    return likelihood(theta, data) * prior(theta)

trace_length = 50000  # The number of jumps to try
burn_in = int(.0 * trace_length)

def metropolis(target_prob, proposal_sd, starting_point, trace_length):
    '''
    Run a simple Metrolopis MCMC algorithm with normal deviated
    proposal.
    '''
    trace = [starting_point]
    while len(trace) < trace_length:
        current_position = trace[-1]
        proposed_jump = np.random.normal(0, proposal_sd)
        proposed_position = current_position + proposed_jump
        current_prob = target_prob(current_position, data)
        proposed_prob = target_prob(proposed_position, data)
        acceptance_prob = min(1, proposed_prob / current_prob)
        if np.random.uniform() < acceptance_prob:
            next_position = proposed_position
        else:
            next_position = current_position
        trace.append(next_position)
    return trace

# Specify standard deviation of proposal distribution
proposal_sd = [0.02, 0.2, 2][0]
trace = metropolis(target_relative_probability, proposal_sd,
                   starting_point=.99, trace_length=trace_length)
# Extract the post-burn-in portion of the trace
accepted_trace = trace[burn_in:]
effective_size = ess(accepted_trace)
acc_ratio = acceptance_ratio(accepted_trace)

plt.subplot(3, 1, 1)
title_template = 'Prpsl.SD == {}; Eff.Sz == {:.1f}'
plt.title(title_template.format(proposal_sd, effective_size))
sns.distplot(accepted_trace)
plt.xlabel('theta')

plt.subplot(3, 1, 2)
plt.title('End of chain')
plt.plot(trace[-100:], range(100))
plt.text(.01, 80, 'Acceptance ratio == {:.3f}'.format(acc_ratio))
plt.xlim([0, 1])
plt.gca().set_yticklabels([])
plt.xlabel('theta')

plt.subplot(3, 1, 3)
plt.title('Beginning of chain')
plt.plot(trace[:100], range(100))
plt.xlim([0, 1])
plt.gca().set_yticklabels([])
plt.tight_layout()
plt.xlabel('theta')

plt.show()
