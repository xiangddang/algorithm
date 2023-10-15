# At most k jumps per run
def max_airtime_distance_with_limit(T, D, k):
    n = len(T)
    
    # Initialize a 2D array to store the maximum airtime distance at each trampoline with up to k jumps.
    max_distance = [[0] * (k + 1) for _ in range(n)]
    print(max_distance)
    # Initialize the first row with the airtime distance for up to k jumps.
    for jumps in range(1, k + 1):
        max_distance[0][jumps] = D[0]
    
    # Iterate through each trampoline and compute the maximum airtime distance for up to k jumps.
    for i in range(1, n):
        for jumps in range(1, k + 1):
            max_distance[i][jumps] = D[i]
            for j in range(i):
                # Check if jumping on this trampoline is beneficial and doesn't exceed the jump limit.
                if T[i] >= T[j] + D[j] and jumps > 1:
                    max_distance[i][jumps] = max(max_distance[i][jumps], max_distance[j][jumps - 1] + D[i])
    
    # Find the maximum airtime distance over all trampolines with up to k jumps.
    print(max_distance)
    max_airtime = max(max_distance[i][k] for i in range(n))
    return max_airtime

# Example usage:
T = [1, 3, 5, 8, 11]
D = [2, 1, 3, 4, 2]
k = 2  # Maximum allowed jumps
result = max_airtime_distance_with_limit(T, D, k)
print(result)  # Output: 7