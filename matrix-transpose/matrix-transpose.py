import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.asarray(A)
    m,n = A.shape
    T = np.zeros((n,m), dtype=A.dtype)
    for i in range(m):
        for j in range(n):
            T[j,i] = A[i,j]
    return T
    pass
