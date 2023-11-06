'''
Let X be a set of n intervals on the real
line. The input, for each 1 ≤ i ≤ n, specifies the start value si and the finish value fi of
interval i. We say that a subset of intervals Y ⊆ X covers X if the union of all intervals
in Y is equal to the union of all intervals in X . The size of a cover is just the number of
intervals. Describe and analyze an efficient algorithm to compute the smallest cover of X.
If you use a greedy algorithm, you must prove that it is correct.
'''
def find_smallest_cover(intervals):
    # Base case: if there's only one interval, it covers itself
    if len(intervals) == 1:
        return 1
    #sort intervals by start values in asc order and final values in desc order
    intervals.sort(key=lambda x: (x[0], -x[1]))
    #Initialize variables
    cover = 1
    end = intervals[0][1]
    new_end = end
    
    for i in range(1, len(intervals)):
        start, finish = intervals[i][0], intervals[i][1]
        if start > end:
            # If the start is greater than 'new_end', increment 'cover' 
            # because a new interval is needed to cover this range.
            if start > new_end:
                cover += 1
                end = finish
                new_end = end
            else:
                # Update 'end' to 'new_end'
                end = new_end
            
        if start <= end:
            if finish > end and new_end == end:
                # Only increment cover when start finding a new interval
                cover += 1
            # Update 'new_end' to be the maximum of 'new_end' and the finish value of the current interval.
            new_end = max(new_end, finish)
        
    return cover
        
    
    
# Test case:
intervals = [(1, 4), (2, 3), (3, 6), (7, 8), (8, 10)]
smallest_cover = find_smallest_cover(intervals)
print(smallest_cover)

intervals = [(1, 5), (2, 6), (3, 7), (8, 10), (9, 12)]
smallest_cover = find_smallest_cover(intervals)
print(smallest_cover)

intervals = [(1, 3), (2, 5), (4, 6), (7, 9), (8, 11), (10, 12)]
smallest_cover = find_smallest_cover(intervals)
print(smallest_cover)