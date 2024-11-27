#!/usr/bin/python3
"""Making Change Problem.
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
                                                                count = 0
                                                                    remaining = total

                                                                        for coin in sorted_coins:
                                                                                    while remaining >= coin:
                                                                                                    remaining -= coin
                                                                                                                count += 1

                                                                                                                    return count if remaining == 0 else -1

