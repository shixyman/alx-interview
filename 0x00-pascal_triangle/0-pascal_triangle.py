#!/usr/bin/python3
def factorial(m):
    if m == 0:
        return 1
    else:
        return m * factorial(m - 1)
    
def pascal_triangle(n):
    for i in range(n):
        row = []
        for j in range(n-i+1):
            print(end="")
        for j in range(i+1):
            coefficient = factorial(i)//(factorial(j)*factorial(i-j))
            row.append(coefficient)
        print(row)