# Graph of normal probability density function, with comb of intervals.
meanval = 0.0
# Specify mean of distribution.
sdval = 0.2
# Specify standard deviation of distribution.
xlow = meanval - sdval # Specify low end of x-axis.
xhigh = meanval + sdval # Specify high end of x-axis.
dx = 0.02
# Specify interval width on x-axis
# Specify comb points along the x axis:
x = seq(from=xlow, to=xhigh, by=dx)
# Compute y values, i.e., probability density at each value of x:
y = (1 / (sdval * sqrt(2 * pi))) * exp(-.5 * ((x - meanval) / sdval) ^ 2)
# Plot the function. "plot" draws the intervals. "lines" draws the bell curve.
xlim = c(-.4, .4)
ylim = c(1, 2)
plot(x, y, type="h", lwd=1, xlim=xlim, ylim=ylim, xlab="x" , ylab="p(x)", main="Normal Probability Density")
lines(x, y)
# Approximate the integral as the sum of width * height for each interval.
area = sum(dx * y)
# Display info in the graph.
prop_text = bquote(paste(
    mu , " = ", .(meanval), ', ', sigma, " = ", .(sdval), ', ', Delta, "x = ", .(dx)
))
text(xlim[1], .9 * ylim[2], prop_text, adj=0)
desc_text = bquote(paste(
    'Mass of [', Mu, ' - ', sigma, ', ', Mu, ' + ', sigma, ']:',
))
sigma_text = bquote(paste(
    sum(,x,),  Delta, "x p(x) = ", .(signif(area,3))
))
text(xlim[2], .9 * ylim[2], desc_text, adj=1)
text(xlim[2], .85 * ylim[2], sigma_text, adj=1, cex=1.2)
