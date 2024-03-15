#!/usr/bin/python3
"""a module that determines prime game"""


def isWinner(x: int, nums: list) -> str:
    """
    A function that determines who wins most rounds
        x: is the number of rounds
        nums: is an array of n
    """
    if x <= 0 or len(nums) == 0:
        return None

    def prime(num: int) -> list:
        """
        A function that generate a prime number
        Args:
            num: is an integer value that set the end bound
        """
        primes = []
        for i in range(2, num + 1):
            is_prime = True
            for j in range(i, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        return primes

    player1 = 0
    player2 = 0
    for rounds in range(x):
        is_prime = prime(nums[rounds])
        if len(is_prime) & 1 == 0:
            player2 += 1
        else:
            player1 += 1
    if player2 > player1:
        return 'Ben'
    if player1 == player2:
        return None
    return 'Maria'
