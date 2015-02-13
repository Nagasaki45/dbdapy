# Specify standard deviation of distribution.
xlow = 0
xhigh = 1
dx = 0.02
# Specify interval width on x-axis
# Specify comb points along the x axis:
x = seq(from=xlow, to=xhigh ,by=dx)
# Compute y values, i.e., probability density at each value of x:
y = 6 * x * (1 - x)
# Approximate the integral as the sum of width * height for each interval.
area = sum(dx * y)
# Plot the function. "plot" draws the intervals. "lines" draws the bell curve.
plot(x, y, type='h', lwd=1, xlab='x', ylab='p(x)', main="Density func for 6x(1 - x)")
lines(x, y)
# Display info in the graph.
text(0, max(y), paste("Approximated integral =", area), adj=0)
