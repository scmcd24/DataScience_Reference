
# Deep Learning Intro

 - Root Mean Square Propagation (RMSprop) Optimizer:
    - Adaptive learning rate
    - Better than AdaGrad at dealing with sparse data / saddles
    - Disadvantages: sensitive to choice of hyperparameters and has optimization
      issues with non-convex data
 - Adam (**ADA**ptive **M**oment Estimation) Optimizer: 
    - Adaptive learning rate (RMSprop) AND momentum
 - Momentum: When calculating next gradient step, past steps are used, not just
   the current