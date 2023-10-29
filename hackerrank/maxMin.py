def maxMin(k, arr):
    # Write your code here
    arr.sort()
    left, right = 0, k - 1
    res = arr[right] - arr[left]
    while right < len(arr):
        res = min(res, arr[right] - arr[left])
        left += 1
        right += 1
    return res