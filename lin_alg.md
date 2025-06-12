
# Linear Algebra

#### Properties of Matrices
 - Singular: square matrix that is not invertible
    - must have at least one eigenvalue == 0
    - Determinant == 0
 - Diagonalizable: matrix is invertible and there exists another diagonal matrix 
   "D" such that D=CAC^-1       where C is an invertible matrix
    - Diagonalizable == all eigenvectors are linearly independent
    - Square
 - Invertible: for a matrix, there exists an inverse that can "undo" its warp
    - A * B = B * A = identity matrix   (matrix * its inverse == identity)
    - Square 


#### Eigenvalues & eigenvectors:
 - Eigendecomposition: A * x = gamma * x
    - Where: A is a square NxN matrix
             x = eigenvector
             gamma = eigenvalue
    - Break matrix into simpler components
    - Each matrix can be thought of has having a direction, LIKE a vector! 
    - Matrices that can decomposed will have an eigenvector, which lies in the
      same plane as the matrix. Eigenvectors are useful because they describe 
      the essence of the matrix (they occupy basically the same space), but they
      are much easier to work with. 
    - When working with eigenvectors, multiplying them by other matrices etc, 
      their direction is not changed. They may be scaled up and down in space - 
      a property called their eigenvalue. An eigenvalue is a scalar - still much
      easier to calculate!
    - Eigenvector: "the effect of the matrix on the vector is the same as the 
      effect of a scalar on the vector."
 - Eigengap: difference between consecutive eigenvalues



#### Matrix special cases:
 - Laplacian: degree matrix - adjacency matrix
 - Jacobian: matrix of first-order partial derivatives
    - Determinant of the square Jacobian == 'Jacobian' determinant


#### References:
 - https://textbooks.math.gatech.edu/ila/diagonalization.html
 - https://builtin.com/data-science/eigendecomposition 
