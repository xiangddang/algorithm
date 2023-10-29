def counterGame(n):
    # Write your code here
    res = 0
    for i in range(63, -1, -1):
        num = 2**i
        if n > num:
            n -= num
            res += 1
    if res % 2 == 1:
        return "Louise"
    else:
        return "Richard"