# Linear & Non-Linear Mixed Modeling

#### Linear Mixed Modeling
- Best for non-independent, multilevel, nested, longitudinal, correlated data
- At the highest level units are independent, but dependent at the unit level
- i.e., patients within a groups (same doctor) vs between groups
- Could just average data from all patients of one doctor, but loss of signal
- Could linear regress each data point, but that's messy

- In linear regression, we could fix our data with the equation y = B0 + B1x1 
  + B2x2 ... + Bnxn
- Therefore, any y value depends soley upon its corresponding x value (its B
  value does not vary, are fixed, constant slopes) >> y1 = B0 + B1 * x1

- What if we know that the intercept varies by group, i.e., each group has a
  different starting point? Random intercepts
    - y1 = B(ij) + B1 * x1
- What if we know that the rate of change of each group differs? Random slopes
    - y1 = B0 + B1(ij) * x1
    - Here, the coefficient is not fixed, but estimated from a distribution of
      coefficients
- What if the starting point and the rate of change both depend on group?
    - y1 = B(ij) + B1(ij) * x1

#### References:
- http://mfviz.com/hierarchical-models/
- https://stats.oarc.ucla.edu/other/mult-pkg/introduction-to-linear-mixed-models/