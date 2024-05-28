def rotate_2d_matrix(matrix):
"""
Rotates a given 2D matrix 90 degrees clockwise in-place.
Args:
matrix (list of lists): The input 2D matrix to be rotated.
Returns:
None
"""
    n = len(matrix)  # Get the size of the matrix (n x n)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            # Swap elements at (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        # Reverse the current row
        matrix[i] = matrix[i][::-1]
