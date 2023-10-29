def lonelyinteger(a):
    # Write your code here
    sum_set = sum(set(a))
    return 2 * sum_set - sum(a)