import numpy as np

# initialize the matrix
A = np.array([[10., -1., 2., 0.],
             [-1., 11., -1., 3.],
             [2., -1., 10., -1],
             [0.0, 3., -1., 8.]])

# initialize the RHS vector
b = np.array([6., 25., -11., 15.])

# prints the system
print("System:")
for i in range(A.shape[0]):
    row = [f"{A[i, j]}*x{j + 1}" for j in range(A.shape[1])]
    print(f'{" + ".join(row)} = {b[i]}')
print()

x = np.zeros_like(b)
ITERATION_LIMIT = 100  # You should define this constant

for it_count in range(ITERATION_LIMIT):
    if it_count != 0:
        print(f"Iteration {it_count}: {x}")
    
    x_new = np.zeros_like(x)
    
    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    
    if np.allclose(x, x_new, atol=1e-5, rtol=0.):
        break
    
    x = x_new

print("Solution:")
print(x)

error = np.dot(A, x) - b
print("Error:")
print(error)
