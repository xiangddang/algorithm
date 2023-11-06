'''
Let X be a set of n intervals on the real
line. The input, for each 1 ≤ i ≤ n, specifies the start value si and the finish value fi of
interval i. A proper coloring of X assigns a color to each interval, so that any two overlapping
intervals are assigned different colors. Describe and analyze an efficient algorithm to compute
the minimum number of colors needed to properly color X. As before, if you use a greedy
algorithm, you must prove that it is correct.
'''
def min_color(intervals):
    if not intervals:
        return 0
    # Sort the intervals by their start values in asc order
    # and final values in desc order
    intervals.sort(key=lambda x: (x[0], -x[1]))
    color_count = 1
    cur_count = color_count
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        start, finish = intervals[i][0], intervals[i][1]
        
        if start <= end:
            # If the current interval overlaps with the previous one, increase the current count
            cur_count += 1
            # Update the color count with the maximum of the current count and the color count
            color_count = max(cur_count, color_count)
            # Update the end with the minimum of the current end and the finish value of the current interval
            end = min(end, finish)
        else:
            # If the current interval doesn't overlap with the previous 
            # one, reset the end and current count
            end = finish
            cur_count = 1

    return color_count

intervals1 = [(1, 3), (4, 6), (7, 9)]
print(min_color(intervals1))

intervals2 = [(1, 4), (2, 5), (6, 9)]
print(min_color(intervals2))

intervals3 = [(1, 5), (2, 4), (3, 6), (4, 8)]
print(min_color(intervals3)) 

intervals4 = [(1, 5)]
print(min_color(intervals4))

intervals5 = [(1, 6), (2, 4), (3, 5)]
print(min_color(intervals5))