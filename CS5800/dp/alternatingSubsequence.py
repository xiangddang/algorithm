'''
 QUESTION:
 Given an array A[1...n] of positive integers, compute the length of the longest alternating subsequence. 
 A sequence P[1..m] is alternating if P[i] < P[i − 1] for every even index i ≥ 2, 
 and if P[i] > P[i − 1] for every odd index i ≥ 3. For example, in the sequence Solution.
 (3,1,4,1,5,9,2,6,5,2,5,8) the longest alternating subsequence is (3,1,4,1,5,2,6,5,8) so we should return 9
'''

def longest_alternating_subsequence_length(A):
    n = len(A)
    
    # Initialize a table to store the length of the longest alternating subsequence ending at each index.
    # We use two arrays, one for increasing and one for decreasing subsequences.
    inc_length = [1] * n  # Length of the longest increasing subsequence ending at index i.
    dec_length = [1] * n  # Length of the longest decreasing subsequence ending at index i.
    
    # Iterate through the array to compute the lengths of alternating subsequences.
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j]:
                inc_length[i] = max(inc_length[i], dec_length[j] + 1)
            elif A[i] < A[j]:
                dec_length[i] = max(dec_length[i], inc_length[j] + 1)
    
    # Find the maximum alternating subsequence length.
    max_length = max(max(inc_length), max(dec_length))
    
    return max_length

# Example usage:
A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 2, 5, 8]
result1 = longest_alternating_subsequence_length(A)
print(result1)  # Output: 9

B = [10, 22, 9, 33, 49, 50, 31, 60]
result2 = longest_alternating_subsequence_length(B)
print(result2)
