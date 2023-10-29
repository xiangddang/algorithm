from collections import Counter

def sockMerchant(n, ar):
    # Write your code here
    count = Counter(ar)
    values = count.values()
    res = 0
    for v in values:
        res += v // 2
    return res