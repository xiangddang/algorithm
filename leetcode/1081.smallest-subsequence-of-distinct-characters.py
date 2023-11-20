#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#

# @lc code=start
import collections

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        remian_counter = collections.Counter(s)
        for c in s:
            if c not in stack:
                while stack and stack[-1] > c and remian_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remian_counter[c] -= 1
        return ''.join(stack)
                
        
# @lc code=end

