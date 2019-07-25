#%% Admin
import numpy as np

# %% BroadCasting
# Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes
# when performing arithmetic operations.
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

# Method 1: Add the vector v to each row of the matrix x with an explicit loop.
for i in range(4):
    y[i, :] = x[i, :] + v
print(y)

# Method 2: Stacking to allow summing
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))   # Stack 4 copies of v on top of each other
print(vv)
y = x + vv
print(y)

# Method 3: Broadcasting
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting
print(y)
