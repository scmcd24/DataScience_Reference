# Linear & Non-Linear Mixed Modeling

#### Linear Mixed Modeling
- Best for non-independent, multi-level, hierarchical, longitudinal, or correlated data
- Units sampled at the highest level are independent, but dependent at the unit level
- i.e., patients within a groups (same doctor) vs between groups
- Could just average data from all patients one doctor saw, but loss of signal
- Could linear regress each data point, but that's messy

- In linear regression, we could fix our data with the equation y = B0 + B1x1 + B2x2 ... + Bnxn
- Linear regression assumes that the beta weights given to each variable are fixed 
- Random intercepts

#### References:
- http://mfviz.com/hierarchical-models/