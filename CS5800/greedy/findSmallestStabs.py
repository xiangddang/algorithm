'''
Let X be a set of n intervals on the real
line. The input, for each 1 ≤ i ≤ n, specifies the start value si and the finish value fi of
interval i. We say that a set P of points stabs X if every interval in X contains at least one
point in P . Describe and analyze an efficient algorithm to compute the smallest set of points
that stabs X. As usual, If you use a greedy algorithm, you must prove that it is correct.
Solution.
'''
def find_smallest_stabs(intervals):
    intervals.sort(key=lambda x: (x[0], -x[1]))
    
    end = intervals[0][1]
    
    count = 1
    for i in range(1, len(intervals)):
        start, finish = intervals[i][0], intervals[i][1]
        if start <= end:
            end = min(end, finish)
        else:
            count += 1
            end = finish
    return count