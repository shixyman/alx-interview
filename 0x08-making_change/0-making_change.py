def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The target amount.
    
    Returns:
        int: The fewest number of coins needed to meet the target amount. If the target amount cannot be met, returns -1.
    """
    # Initialize a list to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make 0 total

    # Iterate through each amount from 1 to the target total
    for amount in range(1, total + 1):
        # Iterate through each coin denomination
        for coin in coins:
            # If the current coin value is less than or equal to the current amount
            if coin <= amount:
                # Update the minimum number of coins needed for the current amount
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the target total cannot be met, return -1
    return dp[total] if dp[total] != float('inf') else -1