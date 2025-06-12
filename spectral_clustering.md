
# Spectral Clustering
# 12JUN2025

#### Steps:
 - Get adjacency matrix of items
    - If you have a graph:  B - C - D
                            | /
                            A
    - Your matrix is composed of the number of nodes/similarity (usually
      Euclidean distance) between pairs:
        |     |  A  |  B  |  C  |  D  |
        -------------------------------
        |  A  |  0  |  1  |  1  |  0  |
        |  B  |  1  |  0  |  1  |  0  |
        |  C  |  1  |  0  |  0  |  1  |       
        |  D  |  0  |  0  |  1  |  0  |
    - Ex, A and B have 1 connection, A and D have 0 connections
 - Get degree matrix of items
    - For each node (A-D), sum the number of connections on the diagonal
        |     |  A  |  B  |  C  |  D  |
        -------------------------------
        |  A  |  2  |  0  |  0  |  0  |
        |  B  |  0  |  1  |  0  |  0  |
        |  C  |  0  |  0  |  3  |  0  |       
        |  D  |  0  |  0  |  0  |  1  |
 - Get the Laplacian matrix: degree - adjacency matrices
        |     |  A  |  B  |  C  |  D  |
        -------------------------------
        |  A  |  0  |  -1 |  -1 |  0  |
        |  B  |  -1 |  1  |  -1 |  0  |
        |  C  |  -1 |  0  |  3  |  -1 |       
        |  D  |  0  |  0  |  -1 |  1  |
 - Eigendecomposition




 - Spectral clustering==kmeans in the kernel space?

#### References:
 - https://eric-bunch.github.io/blog/spectral-clustering