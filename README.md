# Histogram for exponential random variable

Having revised how to compute the median and percentiles you have perhaps already guessed what this next exercise is going to be.  Yes I would like you to estimate the probability density function for the exponential random variable by writing a function to generate this type of random variable and by repeatedly sampling the random variable by calling this function multiple times.  

You should look back on the notes you made last week about computing the histograms for continuous random variables in order to work out how to complete this task as most of the code you need will be the same as the code that we introduced last week.  The one small problem that we have is that the exponential random variable can in theory take any value between 0 and infinity.  The probability of having a very high value for the random variable is, however, very small.  We can thus safely truncate the range and calculate our estimate of the probability density function over some finite range.

Please note that you must set the variable called `lamd` equal to the parameter for the exponential random variable you sample in order to pass the tests for the task.  Furthermore, you must ensure that a graph is plotted using the `plt.plot` and `plt.savefig` commands that appear at the end of the code.
