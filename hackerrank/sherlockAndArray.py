def balancedSums(arr):
    # Write your code here
    summ = sum(arr)
    left = 0
    right = summ - arr[0]
    if left == right:
        return "YES"
    for i in range(1, len(arr)):
        left += arr[i-1]
        right -= arr[i]
        if left == right:
            return "YES"
    return "NO"