def birthday(s, d, m):
    # Write your code here
    left, right = 0, m-1
    res = 0
    summ = sum([s[i] for i in range(0, m)])
    while right < len(s):
        if summ == d:
            res += 1
        right += 1
        left += 1
        if right < len(s):
            summ = summ + s[right] - s[left - 1]
    return res