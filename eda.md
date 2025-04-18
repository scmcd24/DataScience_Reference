
# Getting started
# Variable continous or discrete?

# Univariate (One variable)
## Continuous:

#### Features:
 - Measure of central tendency: mean, median, mode
    - Geometric vs harmonic vs arithmetic means
 - Measure of spread: 
    - Range: maximum - minimum
        - Sensitive to outliers
    - IQR: 3rd quartile - 1st quartile
        - Less sensitive to outliers
    - Variance: 
        - Population: sum((x - M)2) / N 
        - Sample: sum((x - M)2) / N -1
            - Why N-1? 
        - Not in variable units, in variable units squared
    - Standard deviation: sqrt(variance)
        - In variable units
 - Skew: asymmetric or not? Right or left skewed?
    - "The tail tells the tale"
    - Negative/Left skew
        - tail to the left
        - mean < median < mode 
        - indicative of ceiling effects
    - Positive/Right skew
        - tail to the right
        - mode < median < mean 
        - indicative of floor effects
 - Kurtosis: "tailedness", arcing of the distribution
     - Mesokurtic: No (excess) kurtosis == 0, only 1 non-extreme peal
     - Leptokurtic: Positive kurtosis
         - Higher peak / fat tails: Lepto == "slender"
         - Higher probability of getting outliers / risk
         - Image processing: edges or areas with high contrast have high 
           kurtosis
     - Platykurtic: Negative kurtosis
         - Lower peak / flatter tails: Platy == "broad"
 - Outliers/data gaps: z score method, IQR

#### Variable Transforms
 - Minmax scaling
 - Log transform
 - Exponentiated transform
 - Shift R/L?

#### Plots
 - QQ plots (Quantile-Quantile):
    - Compare the quantiles of one probability distribution with another
    - Compare a variable's distribution against normal distribution, ex.

 - Histogram:
     - Shows distribution shape well but not values
        - Binned variable values on x, frequency on y
     - Karl Pearson
     - Shows central tendency, spread, outliers, and distribution shape
         (whether variable is normal or not)
     - Assess the need for variable transforms to achieve normality
     - Can layer density plot on top of histogram

 - Boxplot:
    - Shows distribution values (outliers) well but not shape
    - Solid box: 1st and 3rd quartile
    - Dashed line: mean
    - Solid line inside solid box: median
    - Whiskers above/below box: 1.5 * IQR (anything outside them are outliers)

 - Violin plot:
    - Boxplot + Histogram (see both distribution & values/outliers)
    - Esp. for comparing multiple variables/distributions

 - Density plot:
    - Smoothed histogram: Distribution shape w/o jagged bins
        - Binned variable values on x, prob # for each value on y

 - Other plots:
    - Frequency chart, stem-and-leaf plot, dotplot?, beanplot, shifted histograms

## Categorical

#### Features:
 - Count
 - Proportion
 - Class imbalance
 - Mislabellings

#### Transforms:
 - One-hot-encoding (AKA dummy encoding, dummy variables)

#### Plots:
 - Bar chart:
    - X: Each category    y: count of each category
    - Can also use % of each category instead
        - Do not use a pie chart. like ever
    - Make sure to properly arrange category: months, variable order
    - Quick way to assess for missing/mislabeled data (NAs): impute or exclude

 - Other plots:
    - Cleveland dotplots, lollipop charts: when there are many categories


# Bivariate (two variables)
#### Features:
- Associations
- Outliers
- Clusters
- Gaps
- Change points
- Heteroskedasticity:
    - Is the variance approximately the same across all values of X1 and X2?
    - Transforming variables may help

#### Plots:
 - Scatter plot:
    - Association between two continuous variables
    - X: values on var1    y: values on var2
    - Helps to view strength of relationship, outliers, clusters, linearity,
      heteroskedasticity

 - Strip plot:
    - Scatter plot but between 1 continous and 1 categorical

 - Other plots: hexbin, violin plots, boxplots, overlaid density plots, ridge
   plots, bar charts

# Multivariate (3+ variables)
#### 

#### Plots:
 - Heatmap (AKA correlation matrix):
    - Can also visualize missing values this way

 - Other plots: treemap, PCP, mosiac plot, 



References:
 - This is so good: [https://uc-r.github.io/gda](https://uc-r.github.io/gda)
 - Picture source: https://medium.com/@dancerworld60/kurtosis-and-how-to-find-given-distribution-is-normal-or-not-50ed3b05bf3b
 - Picture skew: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.mdpi.com%2F2813-0464%2F2%2F4%2F42&psig=AOvVaw3MTm3iHuqJapz0iQ2tcj5t&ust=1745076110121000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJiEwp_x4YwDFQAAAAAdAAAAABAE
