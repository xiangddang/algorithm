def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    left = right = 0
    for i in range(n):
        left += arr[i][i]
        right += arr[i][n-i-1]
    return abs(left - right)