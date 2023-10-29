def pageCount(n, p):
    # Write your code here
    if p > n //2:
        if n % 2 == 0 and p % 2 != 0:
            return (n - p)//2 + 1
        else:
            return (n - p) // 2
    else:
        return p // 2
