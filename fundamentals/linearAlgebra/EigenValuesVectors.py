# Eigenvalues and eigenvectors are properties of square matrices.

# Definition
# For a square matrix A, an eigenvector v and an eigenvalue 𝜆 satisfy:
#     Av=λv

# v (Eigenvector): A special vector that does not change direction when multiplied by A.
# λ (Eigenvalue): A scalar that tells how much the eigenvector is stretched or shrunk


# Think of eigenvectors as roads and eigenvalues as speed limits
# If λ>1, the car speeds up (stretched).
# If 0<λ<1, the car slows down (shrunk).
# If λ=−1, the car reverses but moves at the same speed.


# to compute eigenValues (λ) of a vector A  => det(A - λI) = 0
# for eigenVector V => (A - λI)V = 0 
# to computte the eigenvecctor first compute the eigenvalues 


import numpy as np 

A = np.array([[4, -2], [1, 1]])

eigenValues , eigenVectors  = np.linalg.eig(A)
print(eigenVectors)
print(eigenValues)

