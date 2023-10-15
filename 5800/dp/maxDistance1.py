# QUESTION:
# On weekends, Koji enjoys vis- iting a popular trampoline arena. 
# One of the main attractions is a track with trampolines placed at different spots.
# Upon reaching a trampoline on the track, there are two choices. Either sidestep it 
# and continue running, or jump on it. Choosing to jump propels you into the air, 
# allowing you to land at a distance further down the track. While exhilarating, 
# it might result in skipping other trampolines.
# As a challenge, Koji wants to maximize the total airtime distance. Your task is 
# to assist her in achieving this. Formally, you are provided with an array T[1..n] 
# representing the distance of the ith trampoline from the track’s beginning 
# (you can assume T[1] < T[2] < ... < T[n]), and another array D[1..n] that indicates 
# the airtime distance covered when jumping on the ith trampoline.
# For clarity, if one jumps on trampoline i, the airtime covers D[i] distance and landing occurs at T [i] + D[i], from where trampolines can be further taken.

# determines the maximum airtime distance Koji can achieve.O(n2)
def max_airtime_distance_first(T, D):
    n = len(T)
    
    # Initialize a list to store the maximum airtime distance at each trampoline.
    max_distance = [0] * n
    
    # The maximum airtime distance at the first trampoline is the same as the airtime distance.
    max_distance[0] = D[0]
    
    # Iterate through each trampoline and compute the maximum airtime distance.
    for i in range(1, n):
        max_distance[i] = max_distance[i-1]
        for j in range(i):
            # Check if jumping on this trampoline is beneficial.
            if T[i] >= T[j] + D[j]:
                max_distance[i] = max(max_distance[i], max_distance[j] + D[i])
    
    # Find the maximum airtime distance over all trampolines.
    print(max_distance)
    return max_distance[-1]

# Example usage:
T = [1, 3, 5, 8, 11]
D = [2, 1, 3, 4, 2]
result = max_airtime_distance_first(T, D)
print(result)  # Output: 10


T = [1, 3, 4, 7, 10, 13, 14]
D = [3, 2, 3, 2, 3, 4, 2]
result = max_airtime_distance_first(T, D)
print(result)  # Output: 15
