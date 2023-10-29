def countingSort(arr):
    # Write your code here
    hash = [0 for i in range(100)]
    for a in arr:
        hash[a] += 1
    return hash