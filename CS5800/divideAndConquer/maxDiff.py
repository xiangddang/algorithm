def find_min(array, low, high):
    min_index = low
    for i in range(low + 1, high + 1):
        if array[i] < array[min_index]:
            min_index = i
    return min_index

def find_max(array, low, high):
    max_index = low
    for i in range(low + 1, high + 1):
        if array[i] > array[max_index]:
            max_index = i
    return max_index

def max_diff(array, low, high):
    if low < high:
        mid = low + (high - low) // 2
        leftMax, i1, j1 = max_diff(array, low, mid)
        rightMax, i2, j2 = max_diff(array, mid + 1, high)
        minLeft = find_min(array, low, mid)
        maxRight = find_max(array, mid + 1, high)
        max_diff_val = max(leftMax, rightMax, array[maxRight] - array[minLeft])
        if max_diff_val == leftMax:
            return max_diff_val, i1, j1
        elif max_diff_val == rightMax:
            return max_diff_val, i2, j2
        else:
            return max_diff_val, minLeft, maxRight
    return 0, 0, 0

A = [7, 1, 5, 3, 6, 4]
print(max_diff(A, 0, len(A) - 1))
