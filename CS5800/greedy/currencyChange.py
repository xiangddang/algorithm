'''
Suppose you are a cashier and have
unlimited supply of coins of values $1, $5, $10, $25, and $100. Given an amount n in the
input, your task is to pay n with as few coins as possible. The Cashier Exchange algorithm
is a greedy algorithm for this task that works as follows:
'''
def currency_change(coins, N):
    coinset = []
    coin_sum = 0
    coins.sort(reverse=True)
    while coin_sum < N:
        for c in coins:
            if c + coin_sum <= N:
                coinset.append(c)
                coin_sum += c
    return coinset

coins = [1, 5, 10, 25, 100]
print(currency_change(coins, 126))