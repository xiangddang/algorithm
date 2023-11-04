'''
Let X be a set of n intervals on the real
line. The input, for each 1 ≤ i ≤ n, specifies the start value si and the finish value fi of
interval i. We say that a subset of intervals Y ⊆ X covers X if the union of all intervals
in Y is equal to the union of all intervals in X . The size of a cover is just the number of
intervals. Describe and analyze an efficient algorithm to compute the smallest cover of X.
If you use a greedy algorithm, you must prove that it is correct.
'''
def find_smallest_cover(intervals):
    
    
    
# Test case:
intervals = [(1, 3), (2, 4), (3, 6), (5, 7), (8, 9)]
smallest_cover 