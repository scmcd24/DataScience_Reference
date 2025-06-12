
# Kernel Density Estimation (KDE)

 - Non-parametric estimate of the probability density distribution of a function
 - ie., using the points already observed, can we come up with a smooth curve 
   that approximates the overall distribution?

 - Parameters:
    - Bandwith: the width of the kernel function at each point, how many
        observations we'll include in weighting each point
        - Defines "smoothness" of the output curve (higher = wider = smoother)
    - Kernel: weighting function, must be non-negative

 - Formula:
    - f^(x) = Sumx( K*( (x - observation) / bandwidth ) )
    - Where: f^(x) is the kde
             K is the kernel function
             x is the set of values we'll include in the kde
             observations are the set of values we have
             bandwidth is the width

 - How it works:
    - We use our observations to estimate a weight for each point x in the
      output kde distribution. At each point, we apply the kernel function to
      the observations within our bandwidth.
    - For example, if the observed distribution is [1 2 3 4 5], our point is 2, 
      and our bandwidth is 1, our weight for point 2 would include observations
      1, 2, and 3.
    - Note: the set x, values for the output kde distribution, does NOT have to
      be the set of observed values (you could estimate point 6, etc.)
    - Values that are observed more frequently are weighted higher in the kde

 - Kernel Functions:
    - Guassian: most common; more comp $; edge effects due to infinite tails?
    - Epanechnikov: optimizes MSE (mean squared error)? less comp $
    - Uniform: all points given equal weight
    - Triangular: linear weighting (highest at center of bandwidth)
    - Biweght (Quartic): smoother near the edges of data clusters

 - Cross-validation: (least squares): find ideal bandwidth by comparing estimate
   to actual observations

 - Uses:
    - ex: kernel regression, time series (periodogram?), Naive Bayes, visualize
      data more smoothly than histogram

#### See also:
 - Mean-shift clustering

#### References:
 - https://mathisonian.github.io/kde/
 - https://en.wikipedia.org/wiki/Kernel_density_estimation
 - https://www.numberanalytics.com/blog/kernel-density-estimation-complete-guide#kernel-functions
