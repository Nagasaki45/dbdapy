# Gauss func
gauss_func <- function(x, mean, sd) {
    return((1 / (sd * sqrt(2 * pi))) * exp(-.5 * ((x - mean) / sd) ^ 2))
}
# Graph of normal probability density function, with comb of intervals
mean = 162
# Specify mean of distribution
sd = 16
# Specify interval width on x-axis
dx = 1
x = seq(from=mean - 3 * sd, to=mean + 3 * sd, by=dx)
calc_x = seq(from=147, to=177, by=dx)
# Compute y values, i.e., probability density at each value of x:
y = gauss_func(x, mean, sd)
calc_y = gauss_func(calc_x, mean, sd)
# Plot the function. "lines" draws the intervals. "plot" draws the bell curve.
plot(x, y, type='l', xlab='x', ylab='p(x)', main='Normal Probability Density')
lines(calc_x, calc_y, type='h')
# Approximate the integral as the sum of width * height for each interval.
area = sum(dx * calc_y)
# Display info in the graph.
prop_text = bquote(paste(
    mu , " = ", .(mean), ', ', sigma, " = ", .(sd), ', ', Delta, "x = ", .(dx)
))
text(mean - 3 * sd, .9 * max(y), prop_text, adj=0)
desc_text = bquote(paste(
    'Mass of [', .(min(calc_x)), ', ', .(max(calc_x)), ']:',
))
sigma_text = bquote(paste(
    sum(,x,),  Delta, "x p(x) = ", .(signif(area,3))
))
text(mean + 3 * sd, .9 * max(y), desc_text, adj=1)
text(mean + 3 * sd, .85 * max(y), sigma_text, adj=1, cex=1.2)
