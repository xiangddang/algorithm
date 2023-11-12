#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(target, combine, idx):
            if target == 0:
                ans.append(combine)
                return
            if idx == len(candidates):
                return
            dfs(target, combine, idx + 1)
            if target - candidates[idx] >= 0:
                dfs(target - candidates[idx], combine + [candidates[idx]], idx)
        
        dfs(target, [], 0)
        return ans
        
# @lc code=end

