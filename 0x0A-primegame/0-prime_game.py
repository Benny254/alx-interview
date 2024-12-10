#!/usr/bin/python3
"""
Prime Game Solution: Determine the winner of a game where players remove primes and their multiples.
"""

def generate_primes(limit):
        """
            Generates a list of prime numbers up to a given limit.
                Args:
                        limit (int): Upper boundary for prime generation.
                            Returns:
                                    list: A list of prime numbers up to the limit.
                                        """
                                            sieve = [True] * (limit + 1)
                                                sieve[0] = sieve[1] = False  # 0 and 1 are not primes
                                                    primes = []
                                                        for p in range(2, limit + 1):
                                                                    if sieve[p]:
                                                                                    primes.append(p)
                                                                                                for multiple in range(p * p, limit + 1, p):
                                                                                                                    sieve[multiple] = False
                                                                                                                        return primes

                                                                                                                    def isWinner(x, nums):
                                                                                                                            """
                                                                                                                                Determines the overall winner of the Prime Game.
                                                                                                                                    Args:
                                                                                                                                            x (int): Number of rounds.
                                                                                                                                                    nums (list): List of upper limits for each round.
                                                                                                                                                        Returns:
                                                                                                                                                                str: "Maria" if Maria wins, "Ben" if Ben wins, or None if it's a tie.
                                                                                                                                                                    """
                                                                                                                                                                        if not nums or x < 1:
                                                                                                                                                                                    return None

                                                                                                                                                                                    max_n = max(nums)
                                                                                                                                                                                        primes = generate_primes(max_n)
                                                                                                                                                                                            prime_counts = [0] * (max_n + 1)

                                                                                                                                                                                                # Precompute the number of primes up to each number
                                                                                                                                                                                                    for i in range(1, max_n + 1):
                                                                                                                                                                                                                prime_counts[i] = prime_counts[i - 1] + (1 if i in primes else 0)

                                                                                                                                                                                                                    maria_wins = 0
                                                                                                                                                                                                                        ben_wins = 0

                                                                                                                                                                                                                            # Evaluate each round
                                                                                                                                                                                                                                for n in nums:
                                                                                                                                                                                                                                            if prime_counts[n] % 2 == 0:
                                                                                                                                                                                                                                                            ben_wins += 1
                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                    maria_wins += 1

                                                                                                                                                                                                                                                                                        # Determine the overall winner
                                                                                                                                                                                                                                                                                            if maria_wins > ben_wins:
                                                                                                                                                                                                                                                                                                        return "Maria"
                                                                                                                                                                                                                                                                                                        elif ben_wins > maria_wins:
                                                                                                                                                                                                                                                                                                                    return "Ben"
                                                                                                                                                                                                                                                                                                                    return None

