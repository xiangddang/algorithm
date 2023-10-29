# Find the pattern first

def sumXor(n):
    # Write your code here
    res = 1
    while n:
        if n % 2 == 0:
            res *= 2
        n >>= 1
    return res