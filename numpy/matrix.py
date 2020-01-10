import numpy as np
from scipy.sparse import csr_matrix

foo=np.array([[1,2,3],[4,5,6]])
print(foo)

# Sparse
foo_sparse=csr_matrix(foo)
print(foo_sparse)

# Info
print("Sparse Size: ", foo_sparse.size)
print("Sprase Shape: ", foo_sparse.shape)
print("Number of sparse dimensions: ", foo_sparse.ndim)

