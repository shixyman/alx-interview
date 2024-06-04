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
    # Initialize the table with a maximum possible value
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins are needed to make 0 total
    dp[0] = 0

    # Iterate through the amounts from 1 to the target total
    for amount in range(1, total + 1):
        # Iterate through the available coins
        for coin in coins:
            # If the current coin value is less than
            # or equal to the current amount
            if coin <= amount:
                # Update the minimum number of
                # coins needed for the current amount
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the target total cannot be met, return -1
    return dp[total] if dp[total] != float('inf') else -1
