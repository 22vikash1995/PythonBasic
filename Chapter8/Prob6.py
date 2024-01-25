"""
Write a program to add two 3x4 matrices.
"""
# Creating two 3x4 matrices
matric1 = [[1, 2, 3, 4], [5, 6, 7, 8], [8, 7, 5, 6]]
matric2 = [[6, 5, 4, 2], [3, 2, 1, 4], [1, 5, 7, 6]]

# Creating an empty matric
emp_matric = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print(matric1)
print(matric2)
# iterate through rows
for i in range(len(matric1)):
    # iterate through column
    for j in range(len(matric1[0])):
        emp_matric[i][j]=matric1[i][j]+matric2[i][j]

print(emp_matric)