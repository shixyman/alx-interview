#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If it's not possible to meet the total, returns -1.
    """
    # If the total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number
    # of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Iterate through each amount from coin to total
        for i in range(coin, total + 1):
            # Update the minimum number of coins needed for the current amount
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the total cannot be met, return -1
    return dp[total] if dp[total] != float('inf') else -1
