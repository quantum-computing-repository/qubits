import numpy as np

def matrices():

    a1 = np.ndarray(shape=(2,2), dtype=int)
    print(a1)

    a2 = np.zeros(shape=(2,2), dtype=int)
    print(a2)

    a3 = np.identity(3, dtype=int)
    print(a3)

    a4 = np.array([[1, 2], [3, 1]])
    print(a4)

    a5 = np.array([[5, 6], [7, 8]])
    print(a5)

    # matrix multiplication
    a6 = np.matmul(a4, a5)
    print(a6)

    # determinant
    d1 = np.linalg.det(a4)
    print(d1)

    # eigen values and vectors
    w, v = np.linalg.eig(a4)
    print(w, v)

    a7 = np.array([[1], [2]]) # 2x1
    a8 = np.array([[3, 4]])   # 1x2

    # 2x1 x 1x2 = 2x2
    a9 = np.matmul(a7, a8)
    print(a9)

    # tensor product
    a10 = np.array([[1, 2], [3, 4]])
    a11 = np.array([[5, 6], [7, 8]])
    a12 = np.kron(a10, a11)
    print(a12)











