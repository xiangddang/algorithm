#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = sum(gas) - sum(cost)
        if total < 0:
            return -1
        start = 0
        summ = 0
        for i in range(len(gas)):
            summ += gas[i] - cost[i]
            if summ < 0:
                start = i + 1
                summ = 0
        return start
            
# @lc code=end

