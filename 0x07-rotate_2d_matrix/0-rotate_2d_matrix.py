def rotate_2d_matrix(matrix):
"""
Rotates a given 2D matrix 90 degrees clockwise in-place.
Args:
matrix (list of lists): The input 2D matrix to be rotated.
Returns:
None
"""
# Transpose the matrix
for i in range(len(matrix)):
    for j in range(i, len(matrix)):
        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
# Reverse each row in the matrix
for row in matrix:
    row.reverse()
