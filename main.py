import matplotlib.pyplot as plt
import numpy as np

def exponential(lam):
  # Your code to generate an exponential random variable goes here
  
lamd = 2      # The parameter for the exponential random variable you should sample
xmax = 6     # The maximum value for x that you should use in your histogram
nbins = 200   # The number of bins you should use for your histogram
histo = nbins*[0]     # The variable you should use to store the histogram
xvals = nbins*[0]     # The midpoints of your histogram bins that are used for plotting

# Your code to compute an estimate for the probability density function of an exponential random
# variable goes here.


# This draws the histogram - do not delete this code
plt.plot( xvals, histo, 'k-')
plt.savefig("myhistogram.png")
