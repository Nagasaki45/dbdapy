N = 500
n = 1:N  # Flip number vector

p_head = .8  # Probability to get a Head
coinFlips = sample(x=c(0, 1), prob=c(1 - p_head, p_head), size=N, replace=TRUE)
runningAvg = cumsum(coinFlips) / n

# Plot
plot(n, runningAvg, log="x", type='l', ylim=c(0, 1))
lines(c(1, N), c(.8, .8), lty=2)  # Line type = 2 for dashed line. See 'par' help.
# adj=1 let R adjust the x positioning of the text freely
text(N, 0.5, paste("End Proportion =", runningAvg[N]), adj=1)
