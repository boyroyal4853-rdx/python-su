import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

print("Array 1:", arr1)
print("Array 2:", arr2)

# 1. Addition
add = np.add(arr1, arr2)
print("\nAddition:", add)

# 2. Subtraction
sub = np.subtract(arr1, arr2)
print("Subtraction:", sub)

# 3. Multiplication
mul = np.multiply(arr1, arr2)
print("Multiplication:", mul)

# 4. Division
div = np.divide(arr1, arr2)
print("Division:", div)

# 5. Square Root
sqrt = np.sqrt(arr1)
print("Square Root of arr1:", sqrt)

# 6. Power
power = np.power(arr1, 2)
print("Square of arr1:", power)

# 7. Sum of elements
total = np.sum(arr1)
print("Sum of arr1:", total)

# 8. Mean (Average)
mean = np.mean(arr1)
print("Mean of arr1:", mean)

# 9. Maximum & Minimum
print("Max value:", np.max(arr1))
print("Min value:", np.min(arr1))

# 10. Dot Product
dot = np.dot(arr1, arr2)
print("Dot Product:", dot)