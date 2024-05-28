def rotate_2d_matrix(matrix):
"""
Rotates a given 2D matrix 90 degrees clockwise in-place.
Args:
matrix (list of lists): The input 2D matrix to be rotated.
Returns:
None
"""
    # Step 1: Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    
    # Step 2: Reverse each row
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]

