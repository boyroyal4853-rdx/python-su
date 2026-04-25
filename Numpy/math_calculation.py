import numpy as np

# 1. Create arrays
print("=== Array Creation ===")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(0, 10, 2)
arr3 = np.linspace(0, 1, 5)

print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3)


# 2. 2D Array (Matrix)
print("\n=== 2D Array ===")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix)


# 3. Array Properties
print("\n=== Properties ===")
print("Shape:", matrix.shape)
print("Size:", matrix.size)
print("Data Type:", matrix.dtype)


# 4. Indexing & Slicing
print("\n=== Indexing & Slicing ===")
print("First row:", matrix[0])
print("Element (2,3):", matrix[1][2])
print("Column 2:", matrix[:, 1])


# 5. Mathematical Operations
print("\n=== Math Operations ===")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Square:", a ** 2)


# 6. Statistical Functions
print("\n=== Statistics ===")
data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std Dev:", np.std(data))
print("Sum:", np.sum(data))


# 7. Reshaping Arrays
print("\n=== Reshape ===")
arr = np.arange(1, 10)
reshaped = arr.reshape(3, 3)

print("Original:", arr)
print("Reshaped:\n", reshaped)


# 8. Matrix Operations
print("\n=== Matrix Operations ===")
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print("Matrix Multiplication:\n", np.dot(m1, m2))
print("Transpose:\n", m1.T)


# 9. Random Numbers
print("\n=== Random Numbers ===")
rand_arr = np.random.rand(3, 3)
print(rand_arr)


# 10. Filtering (Boolean Indexing)
print("\n=== Filtering ===")
arr = np.array([10, 25, 30, 15, 50])
filtered = arr[arr > 20]

print("Original:", arr)
print("Filtered (>20):", filtered)


# 11. Broadcasting
print("\n=== Broadcasting ===")
arr = np.array([1, 2, 3])
print("Add 10:", arr + 10)


# 12. Save & Load
print("\n=== Save & Load ===")
np.save("data.npy", arr)
loaded = np.load("data.npy")
print("Loaded:", loaded)


print("\n=== Program Finished ===")