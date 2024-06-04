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
    # Base case: If the total is 0, we need 0 coins
    if total == 0:
        return 0

    # Initialize the dp array with a large value
    # (the total + 1, since we can't use more coins than the total)
    dp = [total + 1] * (total + 1)

    # Base case: 0 coins are needed to make 0 total
    dp[0] = 0

    # Iterate through the amounts from 1 to the target total
    for i in range(1, total + 1):
        # Iterate through the available coins
        for coin in coins:
            # If the current coin value is less
            # than or equal to the current amount
            if coin <= i:
                # Update the minimum number of coins needed
                # to make the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the final value in the dp array is greater than the total,
    # it means the target total cannot be met
    return dp[total] if dp[total] <= total else -1
