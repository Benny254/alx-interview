#!/usr/bin/python3
"""Change making module.
"""

def makeChange(coins, total):
        """Determines the fewest number of coins needed to meet a given amount total.
            
                Args:
                        coins (list): A list of the values of the coins in your possession.
                                total (int): The total amount to be met.

                                    Returns:
                                            int: The fewest number of coins needed to meet the total, or -1 if the total cannot be met.
                                                """
                                                    if total <= 0:
                                                                return 0

                                                                sorted_coins = sorted(coins, reverse=True)
                                                                    coins_count = 0
                                                                        remaining = total

                                                                            for coin in sorted_coins:
                                                                                        while remaining >= coin:
                                                                                                        remaining -= coin
                                                                                                                    coins_count += 1

                                                                                                                        return coins_count if remaining == 0 else -1

