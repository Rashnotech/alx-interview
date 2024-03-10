#!/usr/bin/python3
"""a module that make change"""


def makeChange(coins, total):
    """
    coins: a list of values of coins in possession
    total: value to find denomination
    """
    change, num = 0, 0

    if total <= 0:
        return 0
    while change != total:
        rem = total
        new_coin = 0
        for coin in coins:
            if total - (change + coin) < rem and change + coin <= total:
                rem = total - (change + coin)
                new_coin = coin
        if new_coin == 0:
            return -1
        change += new_coin
        num += 1
    return num
