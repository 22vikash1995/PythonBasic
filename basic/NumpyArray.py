import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
for position in arr:
    print(position)

print(np.__version__)
print(type(arr))

tuplearray = np.array(("vikash", "vikky", "vishal", "viswas"))

print(tuplearray)
print(type(tuplearray))

'''
 Dimensions in array
  1. 0-D array
  2. 1-D array
  3. 3-D array
'''
# 0-D or scalars array
arr_0 = np.array(6)
print(arr_0)
# 1-D array
one_d_array = np.array([1, 2, 3, 4, 5, 6])
print("elements of 1-D array is:\n", one_d_array)

# 2-D array
two_d_array = np.array([[1, 2, 3, 4, 5, 6, 7], [9, 8, 6, 5, 4, 3, 2]])
print(two_d_array)

# 3-D array
three_d_array = np.array([[[1, 2], [6, 7]], [["vikash", "vikky", ], ["viswas", "vishal"]]])
print("3-D array elements are:\n ", three_d_array)

# Check Number of dimensions
print(arr_0.ndim)
print(one_d_array.ndim)
print(two_d_array.ndim)
print(three_d_array.ndim)

# Higher Dimensional Arrays
arr = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr)
print("Dimension of array is: ", arr.ndim)

print(three_d_array[1])
print(one_d_array[1])
print(two_d_array[0,0])


arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("Element is: ",arr1[0, 1, 2])
