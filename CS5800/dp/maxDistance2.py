# O(n log n) time (hint: think preprocessing).
def max_airtime_distance(T, D):
    n = len(T)
    
    # Create a list of trampolines sorted by their landing position.
    trampolines = [(T[i] + D[i], D[i]) for i in range(n)]
    trampolines.sort()
    
    # Initialize a list to store the maximum airtime distance at each trampoline.
    max_distance = [0] * n
    
    # The first trampoline has the same airtime distance as its D value.
    max_distance[0] = D[0]
    
    for i in range(1, n):
        # Binary search to find the previous trampoline with a landing position less than or equal to the current one.
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if trampolines[mid][0] <= T[i]:
                left = mid + 1
            else:
                right = mid - 1
        left -= 1
        
        # Calculate the maximum airtime distance by jumping on previous trampolines or starting from scratch.
        max_distance[i] = max(max_distance[left] + D[i], max_distance[i - 1])
    print(max_distance)
    # Return the maximum airtime distance over all trampolines.
    return max_distance[-1]

# Example usage:
T = [1, 3, 5, 8, 11]
D = [2, 1, 3, 4, 2]
result = max_airtime_distance(T, D)
print(result)  # Output: 10


T = [1, 3, 4, 7, 10, 13, 14]
D = [3, 2, 3, 2, 3, 4, 2]
result = max_airtime_distance(T, D)
print(result)  # Output: 15

T = [1, 3, 5, 7, 11, 15]
D = [2, 3, 4, 5, 3, 6]
result = max_airtime_distance(T, D)
print(result)  # Output: 16