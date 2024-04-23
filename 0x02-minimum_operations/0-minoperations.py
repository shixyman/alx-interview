#!/usr/bin/python3
"""
Contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


# def minOperations(n: int) -> int:
#     if n == 1:
#         return 0

#     operations = [float('inf')] * (n + 1)
#     operations[1] = 0

#     for i in range(2, n + 1):
#         if n % i == 0:
#             operations[i] = i
#             for j in range(2, int(i ** 0.5) + 1):
#                 if i % j == 0:
#                     operations[i] = min(operations[i], operations[j] + i // j)

#     return operations[n] if operations[n] != float('inf') else 0


def minOperations(n):
    if n == 1:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0