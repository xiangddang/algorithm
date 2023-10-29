def miniMaxSum(arr):
    # Write your code here
    summ = sum(arr)
    minm = min(arr)
    maxm = max(arr)
    print("%d %d" % (summ - maxm, summ - minm))