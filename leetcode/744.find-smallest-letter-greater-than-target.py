#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        count = float('inf')
        for i in range(len(letters)):
            diff = ord(letters[i]) - ord(target)
            if diff > 0:
                count = min(count, diff)
        return chr(count + ord(target)) if count != float('inf') else letters[0]
        
# @lc code=end

