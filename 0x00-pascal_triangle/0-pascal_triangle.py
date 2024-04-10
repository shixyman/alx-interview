#!/usr/bin/python3
'''
Returns list representing the Pascal's triangle of n
'''


def pascal_triangle(n):
    '''returns empty list if n <= 0'''
    if n <= 0:
        return []

    triangle = []
    row = []
    bef_row = []
    for i in range(0, n + 1):
        row = [j > 0 and j < i - 1 and i > 2 and bef_row[j-1] +
               bef_row[j] or 1 for j in range(0, i)]
        bef_row = row
        triangle += [row]
    return triangle[1:]


# #!/usr/bin/python3
# def factorial(m):
#     if m == 0:
#         return 1
#     else:
#         return m * factorial(m - 1)
    
# def pascal_triangle(n):
#     for i in range(n):
#         row = []
#         for j in range(n-i+1):
#             print(end="")
#         for j in range(i+1):
#             coefficient = factorial(i)//(factorial(j)*factorial(i-j))
#             row.append(coefficient)
#         print(row)