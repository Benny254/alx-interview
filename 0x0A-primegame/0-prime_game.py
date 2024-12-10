#!/usr/bin/python3
"""
Define isWineer function, a solution to the Prime Game problem
"""

def isWinner(x, nums):
        def sieve_of_eratosthenes(limit):
                    """Generates a list where prime[i] is True if i is a prime number."""
                            prime = [True] * (limit + 1)
                                    prime[0] = prime[1] = False  # 0 and 1 are not primes
                                            for i in range(2, int(limit ** 0.5) + 1):
                                                            if prime[i]:
                                                                                for j in range(i * i, limit + 1, i):
                                                                                                        prime[j] = False
                                                                                                                return prime

                                                                                                                def count_primes_up_to(n, prime):
                                                                                                                            """Counts the number of primes up to n."""
                                                                                                                                    return sum(prime[:n + 1])

                                                                                                                                    if not nums or x < 1:
                                                                                                                                                return None

                                                                                                                                                max_n = max(nums)
                                                                                                                                                    prime = sieve_of_eratosthenes(max_n)
                                                                                                                                                        maria_wins = 0
                                                                                                                                                            ben_wins = 0

                                                                                                                                                                for n in nums:
                                                                                                                                                                            primes = count_primes_up_to(n, prime)
                                                                                                                                                                                    if primes % 2 == 0:
                                                                                                                                                                                                    ben_wins += 1
                                                                                                                                                                                                            else:
                                                                                                                                                                                                                            maria_wins += 1

                                                                                                                                                                                                                                if maria_wins > ben_wins:
                                                                                                                                                                                                                                            return "Maria"
                                                                                                                                                                                                                                            elif ben_wins > maria_wins:
                                                                                                                                                                                                                                                        return "Ben"
                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                    return None

