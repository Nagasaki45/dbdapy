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
data = [0] * 6 + [1] * 14

def likelihood(theta, data):
    '''Bernoulli likelihood function'''
    if theta > 1 or theta < 0:
        return 0
    z = sum(data)
    N = len(data)
    return theta ** z * (1 - theta) ** (N - z)

# Define the prior density function
prior = stats.beta(1, 1).pdf

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

# Run the whole MCMC for different proposal SDs
for proposal_sd in [0.02, 0.2, 2]:
    trace = metropolis(target_relative_probability, proposal_sd,
                       starting_point=.1, trace_length=trace_length)
    # Extract the post-burn-in portion of the trace
    accepted_trace = trace[burn_in:]

    plt.figure(figsize=(10, 10))

    # Plot results for different lags
    for column, example_lag in enumerate([2, 5, 10], start=1):

        # Lag example plots of traces and spread
        truncated_trace = accepted_trace[:100]
        head_trace = truncated_trace[:-example_lag]
        tail_trace = truncated_trace[example_lag:]

        # Lags to compute autocorrelation for
        x_range = list(range(1, 31))
        autocorrelation = [acf(accepted_trace, lag) for lag in x_range]

        # Plotting
        plt.subplot(3, 3, column)
        plt.plot(head_trace)
        plt.plot(tail_trace)
        plt.title('Lag == {}'.format(example_lag))

        example_lag_acf = autocorrelation[example_lag - 1]
        plt.subplot(3, 3, column + 3)
        plt.scatter(tail_trace, head_trace)
        plt.title('ACF({}) == {:.3f}'.format(example_lag, example_lag_acf))
        plt.ylim([0, 1])
        plt.xlim([0, 1])
        plt.xlabel('lagged value')
        plt.ylabel('value')

    # Autocorrelation plotting
    plt.subplot(3, 1, 3)
    plt.bar(x_range, autocorrelation)
    plt.title('Trace autocorrelation')
    plt.xlabel('lag')
    plt.ylabel('ACF')

    plt.tight_layout()

    proposal_txt = str(proposal_sd).replace('.', '_')
    filename_template = 'figures/ex02_sd{}.png'
    plt.gcf().savefig(filename_template.format(proposal_txt, example_lag))
