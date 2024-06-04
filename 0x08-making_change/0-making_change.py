#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    
    Args:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount you are trying to make change for.
    
    Returns:
    int: The fewest number of coins needed to meet the total.
        If it is not possible to make change for the total, returns -1.
    """
    # Base case: If the total is 0, we need 0 coins
    if total == 0:
        return 0
    
    # Initialize a list to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Iterate through the amounts from 1 to the total
    for amount in range(1, total + 1):
        # Iterate through the available coins
        for coin in coins:
            # If the current coin value is less than or equal to the current amount
            if coin <= amount:
                # Update the minimum number of coins needed for the current amount
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If the final value in the dp list is still infinity, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
