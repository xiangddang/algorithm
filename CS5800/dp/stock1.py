# limit of k transactions
# can not buy if you already have a stock

def stock(arr, k):
    n = len(arr)
    profit = [[0] * (n + 1) for _ in range(k + 1)]

    for t in range(1, k+1):
        for i in range(2, n + 1):
            profit[t][i] = profit[t][i - 1]
            for j in range(1, i):
                profit[t][i] = max(profit[t][i], arr[i - 1] - arr[j - 1] + profit[t - 1][j - 1])
    print(profit)
    return profit[k][-1]

arr = [100, 200, 250, 330, 40, 30, 700, 400]
k = 2
print(stock(arr, k))