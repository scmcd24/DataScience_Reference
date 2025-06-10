
# K-Nearest Neighbors

#### Assumptions:
 - non-parametric, supervised learning
 - Used for regression and classification tasks

#### Parameters:
 - k: Number of surrounding values to use in classifying each point
        Lower k == higher variance, less bias
        Use an odd k value to avoid ties
 - Distance metric: Euclidean, Manhattan, etc. 

    
 - Distributions with more outliers >> use higher k

#### Advantages:
 - Simple to understand/use

#### Disadvantages:
 - Very computationally expensive: all items stored in memory
 - Curse of dimensionality: feature selection / dimensionality reduction 
   recommended prior to use
 - Prone to overfitting (due to dimensionality problem, bigger concern with 
   lower k values)

#### Uses:
 - Recommendation systems
 - Missing value imputation?
 - Risk (finance)
 - Pattern recognition (text, images)

#### References:
 - https://www.ibm.com/think/topics/knn 