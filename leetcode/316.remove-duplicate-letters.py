#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        import collections
        remian_counter = collections.Counter(s)
        
        for c in s:
            if c not in stack:
                while stack and stack[-1] > c and remian_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remian_counter[c] -= 1
        return ''.join(stack)
        
        
# @lc code=end

