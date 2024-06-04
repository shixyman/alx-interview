def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The target amount.
    
    Returns:
        int: The fewest number of coins needed to meet the target amount. If the target amount cannot be met, returns -1.
    """
    # Initialize the table with max value (total + 1) to represent "impossible"
    dp = [total + 1] * (total + 1)
    
    # Base case: 0 coins are needed to make 0 total
    dp[0] = 0
    
    # Fill the table
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If the target amount cannot be met, return -1
    return dp[total] if dp[total] <= total else -1