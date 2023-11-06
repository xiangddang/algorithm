'''
Let X be a set of n intervals on the real
line. The input, for each 1 ≤ i ≤ n, specifies the start value si and the finish value fi of
interval i. We say that a set P of points stabs X if every interval in X contains at least one
point in P . Describe and analyze an efficient algorithm to compute the smallest set of points
that stabs X. As usual, If you use a greedy algorithm, you must prove that it is correct.
Solution.
'''
def find_smallest_stabs(intervals):
    if len(intervals) == 1:
        return 1
    # Sort the intervals by their start values in asc order and final values in desc order
    intervals.sort(key=lambda x: (x[0], -x[1]))
    # Initialize end with the finish value of the first interval
    end = intervals[0][1]
    # Initialize count to 1
    count = 1
    for i in range(1, len(intervals)):
        start, finish = intervals[i][0], intervals[i][1]
        # If the start <= end, it means the current interval intersects with previous intervals
        if start <= end:
            # According to greedy algorithm, update end
            end = min(end, finish)
        else:
            # if start if greater than end, we need to add a new point
            count += 1
            # update end to be the finish value of the current interval
            end = finish
    return count