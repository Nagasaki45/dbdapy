source('../utils/HDIofGrid.R')
source('../utils/BernGrid.R')

theta = seq(0, 1, length=5)     # Sparse teeth for theta.
p_theta = pmin(theta, 1-theta)  # Triangular shape for p_theta.
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
data = c(rep(0,0),rep(1,1))     # Single flip with 1 head

posterior = BernGrid(theta, p_theta, data, plotType="Bars", 
                     showCentTend="None", showHDI=FALSE, showpD=FALSE)
#------------------------------------------------------------------------------

theta = seq(0, 1, length=11)    # Sparse teeth for theta.
p_theta = pmin(theta, 1-theta)  # Triangular shape for p_theta.
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
data = c(rep(0,0),rep(1,1))     # Single flip with 1 head

posterior = BernGrid(theta, p_theta, data, plotType="Bars", 
                     showCentTend="None", showHDI=FALSE, showpD=FALSE)
#------------------------------------------------------------------------------

theta = seq(0, 1, length=1001)  # Fine teeth for theta.
p_theta = rep(1,length(theta))  # Uniform (horizontal) shape for p_theta.
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
data = c(rep(0,0),rep(1,1))     # Single flip with 1 head

posterior = BernGrid(theta, p_theta, data, plotType="Bars", 
                     showCentTend="None", showHDI=FALSE, showpD=FALSE)
#------------------------------------------------------------------------------

theta = seq(0, 1, length=1001)  # Fine teeth for theta.
p_theta = rep(0,length(theta))  # Only extremes are possible!
p_theta[2] = 1                  # Only extremes are possible!
p_theta[length(p_theta)-1] = 1       
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
data = c(rep(0,0),rep(1,1))     # Single flip with 1 head

posterior = BernGrid(theta, p_theta, data, plotType="Bars", 
                     showCentTend="None", showHDI=FALSE, showpD=FALSE)
#------------------------------------------------------------------------------



theta = seq(0, 1, length=1001)  # Fine teeth for theta.
p_theta = pmin(theta, 1-theta)  # Triangular shape for p_theta.
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
data = c(rep(0,3),rep(1,1))     # 25% heads, N=4

posterior = BernGrid(theta, p_theta, data, plotType="Bars", 
                     showCentTend="Mode", showHDI=TRUE, showpD=FALSE)
#------------------------------------------------------------------------------

theta = seq(0, 1, length=1001)  # Fine teeth for theta.
p_theta = pmin(theta, 1-theta)  # Triangular shape for p_theta.
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
p_theta = p_theta^10            # Sharpen p_theta !
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
data = c(rep(0,3),rep(1,1))     # 25% heads, N=4

posterior = BernGrid(theta, p_theta, data, plotType="Bars", 
                     showCentTend="Mode", showHDI=TRUE, showpD=FALSE)
#------------------------------------------------------------------------------

theta = seq(0, 1, length=1001)  # Fine teeth for theta.
p_theta = pmin(theta, 1-theta)  # Triangular shape for p_theta.
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
p_theta = p_theta^0.1           # Flatten p_theta !
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
data = c(rep(0,3),rep(1,1))     # 25% heads, N=4

posterior = BernGrid(theta, p_theta, data, plotType="Bars", 
                     showCentTend="Mode", showHDI=TRUE, showpD=FALSE)
#------------------------------------------------------------------------------


theta = seq(0, 1, length=1001)  # Fine teeth for theta.
p_theta = pmin(theta, 1-theta)  # Triangular shape for p_theta.
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
data = c(rep(0,30),rep(1,10))   # 25% heads, N=40

posterior = BernGrid(theta, p_theta, data, plotType="Bars", 
                     showCentTend="Mode", showHDI=TRUE, showpD=FALSE)
#------------------------------------------------------------------------------

theta = seq(0, 1, length=1001)  # Fine teeth for theta.
p_theta = pmin(theta, 1-theta)  # Triangular shape for p_theta.
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
p_theta = p_theta^10            # Sharpen p_theta !
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
data = c(rep(0,30),rep(1,10))   # 25% heads, N=40

posterior = BernGrid(theta, p_theta, data, plotType="Bars", 
                     showCentTend="Mode", showHDI=TRUE, showpD=FALSE)
#------------------------------------------------------------------------------

theta = seq(0, 1, length=1001)  # Fine teeth for theta.
p_theta = pmin(theta, 1-theta)  # Triangular shape for p_theta.
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
p_theta = p_theta^0.1           # Flatten p_theta !
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
data = c(rep(0,30),rep(1,10))   # 25% heads, N=40

posterior = BernGrid(theta, p_theta, data, plotType="Bars", 
                     showCentTend="Mode", showHDI=TRUE, showpD=FALSE)
#------------------------------------------------------------------------------

theta = seq(0, 1, length=1000)  # Fine teeth for theta.
# Two triangular peaks on a small non-zero floor:
p_theta = c(rep(1,200),seq(1,100,length=50),seq(100,1,length=50),rep(1,200), 
            rep(1,200),seq(1,100,length=50),seq(100,1,length=50),rep(1,200))
p_theta = p_theta/sum(p_theta)  # Make p_theta sum to 1.0
data = c(rep(0,13),rep(1,14)) 

posterior = BernGrid(theta, p_theta, data, plotType="Bars", 
                     showCentTend="None", showHDI=FALSE, showpD=FALSE)
#------------------------------------------------------------------------------
