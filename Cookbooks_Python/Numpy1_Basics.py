#%% Admin
import numpy as np

#%% Arrays
a = np.array([1, 2, 3])         # Create a rank 1 array
print(type(a))                  # Prints "<class 'numpy.ndarray'>"
print(a.shape)                  # Prints "(3,)"
print(a[0], a[1], a[2])         # Prints "1 2 3"
a[0] = 5                        # Change an element of the array
print(a)                        # Prints "[5, 2, 3]"

b = np.array([[1, 2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"


a = np.zeros((2,2))   # Create an array of all zeros
print(a)
b = np.ones((1,2))    # Create an array of all ones
print(b)              # Prints "[[ 1.  1.]]"
c = np.full((2,2), 7)  # Create a constant array
print(c)
d = np.eye(2)         # Create a 2x2 identity matrix
print(d)
e = np.random.random((2,2))  # Create an array filled with random values
print(e)

#%% Indexing
# Note the mutability! A slice of an array is a view into the same data, so modifying it
# will modify the original array.
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[:2, 1:3]
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77" due to mutability!


# Integer Indexing and Slice Indexing. Yields an array of lower rank than the original array
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the original array:
a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)  # Prints "[[ 2  6 10]] (3, 1)"

# Integer Array Indexing.
# This allows us to construct arbitrary arrays using the data from another array.
a = np.array([[1,2],
              [3, 4],
              [5, 6]])
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"
print(a[[0, 0], [1, 1]])  # Prints "[2 2]"
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"


a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(a)
b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"
a[np.arange(4), b] += 10
print(a)


# Boolean Array Iundexing
a = np.array([[1,2], [3, 4], [5, 6]])

bool_idx = (a > 2)
print(bool_idx)

print(a[bool_idx])  # Prints "[3 4 5 6]"
print(a[a > 2])     # Prints "[3 4 5 6]"
print(a[a > 2])     # Prints "[3 4 5 6]"


# %% DataTypes
x = np.array([1, 2])   # Let numpy choose the datatype
print(x.dtype)         # Prints "int64"
x = np.array([1.0, 2.0])   # Let numpy choose the datatype
print(x.dtype)             # Prints "float64"
x = np.array([1, 2], dtype=np.int64)   # Force a particular datatype
print(x.dtype)


# %% Array Math
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
print(x + y)
print(np.add(x, y))
# Elementwise difference; both produce the array
print(x - y)
print(np.subtract(x, y))
# Elementwise product; both produce the array. Note this is not matrix multiplication
print(x * y)
print(np.multiply(x, y))
# Elementwise division; both produce the array
print(x / y)
print(np.divide(x, y))
# Elementwise square root; produces the array
print(np.sqrt(x))


# %% Vector-ish stuff
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))
# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))
# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))

x = np.array([[1,2],[3,4]])
print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

# Tranposing
x = np.array([[1,2], [3,4]])
print(x)
print(x.T)
v = np.array([1,2,3])  # Note that taking the transpose of a rank 1 array does nothing:
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"