def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The target amount.
    Returns:
    int: The fewest number of coins needed to meet the target amount.
        If the target amount cannot be met, returns -1.
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the target total cannot be met, return -1
    return dp[total] if dp[total] != float('inf') else -1
