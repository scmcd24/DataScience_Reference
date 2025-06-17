
# Deep Learning Intro

#### Properties:
 - VERY nonlinear, non-parametric
 - Input layer: the data you pass
 - Hidden layers: transform the data and extract high-level features
   - Biases, weights, & activation functions are applied to nodes (data points),
     which are selectively passed to next layer. Transforming nodes as such 
     gives new information as we go layer to layer (like a conveyer belt)
   - **AKA forward propogation**:
   - EX: let's say we were observing a toy factory that makes rocking horses and
     model trucks. At the beginning of their conveyor, we'd see raw wood formed
     into separate pieces, then decorated and painted, then assembled; As we go
     layer by layer, we gain additional information about our final object. The
     information we gather - texture, shape, colors, etc - are the 'features' of
     our data
   - Deep learning models are referred to as "black box" because we ask our
     models to determine them for us (like if we set our assembly line to 'auto-
     pilot'). The model estimates millions of parameters (weights/biases applied
     to nodes), which gives DL the edge in creating specific solutions to 
     problems. This also means that we can't track how they arrive at their 
     solution
 - Output layer: a formula to transform the high-level features you found back 
   into the desired result for this task: classified samples, regression, etc

#### Optimizers
 - Root Mean Square Propagation (RMSprop) Optimizer:
    - Adaptive learning rate
    - Better than AdaGrad at dealing with sparse data / saddles
    - Disadvantages: sensitive to choice of hyperparameters and has optimization
      issues with non-convex data
 - Adam (**ADA**ptive **M**oment Estimation) Optimizer: 
    - Adaptive learning rate (RMSprop) AND momentum

#### Loss Functions:
 - Loss function: formula to determine the difference between the model's output
   and the ground truth
   - Rectified Linear Unit (ReLU):
   - Sigmoid:
   - Softmax: 
   - Tversky:
      - 

#### Other
 - Momentum: When calculating next gradient step, past steps are used, not just
   the current
 - Backpropogation (**Back**ward **propogation** of error):
    - 

#### References:
 - https://www.v7labs.com/blog/deep-learning-guide
 - https://en.wikipedia.org/wiki/Tversky_index
